import reference as ref
import math as math
import pandas as pd

debug = True

class Score:

    def speed_in_fifths(self, minute, second, fifths):
        min_fifth = int(minute) * 60 * 5
        sec_fifth = int(second) * 5
        total_fifths = min_fifth + sec_fifth + int(fifths)
        return total_fifths

    def time_split(self, time):
        min = time.split(':', 3)[0]
        sec = time.split(':', 3)[1]
        fif = time.split(':', 3)[2]
        return min, sec, fif

    def speed_track_adjusted(self, actual_speed, from_track, to_track):

        if debug: print(f'     Unadjusted speed is {actual_speed}')

        act_min, act_sec, act_fif = Score().time_split(actual_speed)
        from_min, from_sec, from_fif = Score().time_split(from_track)
        to_min, to_sec, to_fif = Score().time_split(to_track)
        conversion = (Score().speed_in_fifths(from_min, from_sec, from_fif) - Score().speed_in_fifths(to_min, to_sec, to_fif))
        actual = Score().speed_in_fifths(act_min, act_sec, act_fif)
        final = actual - conversion
        if final > 0:
            minute = math.floor(final / (60 * 5))
            second = math.floor((final - (minute * 60 * 5)) / 5)
            fifth = (final - (minute * 60 * 5) - (second * 5))
        elif final < 0:
            minute = math.ceil(final / (60 * 5))
            second = math.ceil((final - (minute * 60 * 5)) / 5)
            fifth = (final - (minute * 60 * 5) - (second * 5))

        if len(str(second)) == 1:
            second = '0'+str(second)
        else:
            second = str(second)

        if debug: print(f'     Adjusted speed is {minute}:{second}:{fifth}')

        return minute, second, fifth

    def calc_speed_points(self, minute, second, fifths):
        speed = f'{minute}:{second}'
        initial_speed_points = ref.speed_points_lu.loc[ref.speed_points_lu['speed'] == speed, ['points']]['points'].values[0]
        final_speed_points = initial_speed_points - int(fifths)

        if debug: print(f'Speed points = {final_speed_points}')

        return final_speed_points

    def calc_effort_points(self, post_position, postion_at_quarter, parked_out):
        position_change = post_position[0]+postion_at_quarter[0]

        if ref.effort_from_outside_lu.post_to_quarter.eq(position_change).any():
            change_points = ref.effort_from_outside_lu.loc[ref.effort_from_outside_lu['post_to_quarter'] == position_change, ['points']]['points'].values[0]
        else:
            change_points = 0

        if pd.notnull(parked_out):
            parked_out_points = ref.parked_out_points_lu.loc[ref.parked_out_points_lu['parked'] == parked_out, ['points']]['points'].values[0]
        else:
            parked_out_points = 0

        effort_points = change_points + parked_out_points

        if debug: print(f'     Effort - Change Points = {change_points}')
        if debug: print(f'     Effort - Parked Out Points = {parked_out_points}')
        if debug: print(f'Effort - Total Effort Points = {effort_points}')

        return effort_points

    def calc_stretch_finish(self, parked_out, lengths_gained_in_stretch):

        # this is the same calc as for effort above. Should remove duplication.
        if pd.notnull(parked_out):
            parked_out_points = \
            ref.parked_out_points_lu.loc[ref.parked_out_points_lu['parked'] == parked_out, ['points']]['points'].values[
                0]
        else:
            parked_out_points = 0

        lengths_gained_in_stretch = int(lengths_gained_in_stretch)

        if parked_out_points >= 6 and lengths_gained_in_stretch > 0:
            sf_points = 4 + lengths_gained_in_stretch
        elif parked_out_points == 4 and lengths_gained_in_stretch > 0:
            sf_points = 2 + lengths_gained_in_stretch
        elif parked_out_points >= 6 and lengths_gained_in_stretch == 0:
            sf_points = 4
        elif parked_out_points == 4 and lengths_gained_in_stretch == 0:
            sf_points = 2
        elif (parked_out_points >= 6 or parked_out_points == 4) and lengths_gained_in_stretch < 0:
            sf_points = 0
        elif parked_out_points == 0 and lengths_gained_in_stretch > 5:
            sf_points = 5
        elif parked_out_points == 0 and lengths_gained_in_stretch < -5:
            sf_points = -5
        elif parked_out_points == 0:
            sf_points = lengths_gained_in_stretch
        else:
            print('Error: Unexpected Effort and Lengths Gained Combination')

        if debug: print(f'Stretch and Finish - Total SF Points = {sf_points}')

        return sf_points

    def calc_last_race_odds(self, last_race_favourite, last_race_outcome, equivalent_odds):
        # If else statements to assign points based on whether the horse was a fave / won their last race.
        # There is a sentence saying to give three points, win or lose, to a horse with less than 2 eq odds. Seems odd?
        if float(equivalent_odds) <= 2:
            odds_points = 3
        elif last_race_favourite == 'yes' and last_race_outcome == 'win':
            odds_points = 3
        elif last_race_favourite == 'yes' and last_race_outcome == 'lose':
            odds_points = 5
        else:
            odds_points = 0


        if debug: print(f'Last Race Odds Points = {odds_points}.')
        return odds_points

