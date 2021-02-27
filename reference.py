import pandas as pd

data = {'speed': ['1:58',
                '1:59',
                '2:00',
                '2:01',
                '2:02',
                '2:03',
                '2:04',
                '2:05',
                '2:06',
                '2:07',
                '2:08',
                '2:09',
                '2:10',
                '2:11',
                '2:12',
                '2:13',
                '2:14'
                ],
        'points': [80, 75, 70, 65, 60, 55, 50,  45, 40, 35, 30, 25, 20, 15, 10, 5, 0]}
speed_points_lu = pd.DataFrame(data)

parked_data = {'parked': ['1w1q', '1w2q', '1w3q', '1w2q_nc', '2w1q', '2w2q', '2w1q_1w1q', '2w2q_1w1q', '2w1q_1w2q'],
               'points': [4, 7, 10, 8, 6, 12, 9, 14, 13]}
parked_out_points_lu = pd.DataFrame(parked_data)

effort_from_outside = {'post_to_quarter': ['51', '61', '52', '62', '71', '81', '72', '82', '73', '83', '74', '84'],
                       'points': [1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2]}
effort_from_outside_lu = pd.DataFrame(effort_from_outside)

# if __name__ == "__main__":
#     print(speed_points_lu)
#     print(parked_out_points_lu)
#     print(effort_from_outside_lu)