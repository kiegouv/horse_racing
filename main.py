import horse_fn as fn
import numpy as np


class Horse:
    def __init__(self,
                 horse_name,
                 horse_time,
                 from_track_time,
                 to_track_time,
                 post_position,
                 postion_at_quarter,
                 parked_out,
                 lengths_gained_in_stretch):
        self.horse_name = horse_name
        self.horse_time = horse_time
        self.from_track_time = from_track_time
        self.to_track_time = to_track_time
        self.horse_post_position = post_position,
        self.horse_position_at_quarter = postion_at_quarter,
        self.horse_parked_out = parked_out
        self.horse_lengths_gained_in_stretch = lengths_gained_in_stretch


    def calculate(self):
        print(f'\n')
        print(f'Your horse is named {self.horse_name}')
        minute, second, fifth = score.speed_track_adjusted(self.horse_time, self.from_track_time, self.to_track_time)
        speed = score.calc_speed_points(minute, second, fifth)
        effort = score.calc_effort_points(self.horse_post_position, self.horse_position_at_quarter, self.horse_parked_out)
        stretch_finish = score.calc_stretch_finish(self.horse_parked_out, self.horse_lengths_gained_in_stretch)



if __name__ == "__main__":
    score = fn.Score()
    horse1 = Horse(horse_name="Starlight",
                   horse_time="2:06:1",
                   from_track_time="2:04:1",
                   to_track_time="2:02:1",
                   post_position='8',
                   postion_at_quarter='4',
                   parked_out='1w2q_nc',
                   lengths_gained_in_stretch = '2')
    horse2 = Horse(horse_name="Bonnie Bunny",
                   horse_time="2:10:0",
                   from_track_time="2:05:3",
                   to_track_time="2:04:2",
                   post_position='7',
                   postion_at_quarter='4',
                   parked_out='1w1q',
                   lengths_gained_in_stretch='10'
                   )
    horse3 = Horse(horse_name="Drunken Pony",
                   horse_time="2:10:0",
                   from_track_time="2:04:2",
                   to_track_time="2:05:3",
                   post_position='7',
                   postion_at_quarter='4',
                   parked_out=np.nan,
                   lengths_gained_in_stretch='6'
                   )
    horse1.calculate()
    horse2.calculate()
    horse3.calculate()

        #
        #
        # f'Its speed is {self.horse_speed_min}:{self.horse_speed_sec}:{self.horse_speed_fifth_sec}'
        # f'\nSpeed points assigned = {score.calc_speed_points(self.horse_speed_min, self.horse_speed_sec, self.horse_speed_fifth_sec)}')