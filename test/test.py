import tennisroster.context

ctx = tennisroster.context.Context("context.json")

ctx.load_input_data("samplelist.xlsx", 1)

ctx.create_matchups()

vals = ctx.get_match_list(2)

print(vals)

points = [(1,2)] * len(vals)
sub_points = [(15, 30)]* len(vals)

ctx.update_scores(2, points, sub_points)

# import json
#
# y = {"TennisRoster": [{"Teams": [1,2,3],
#                 "Points": [1,2,3],
#                 "Sub_pts": [1,2,3]
#                  }]
#      }
# y2 = {"Teams": [1,2,3],
#     "Points": [1,2,3],
#     "Sub_pts": [1,2,3]
#     }
#
# f = open('context.json', 'r+')
#
# json.dump(y, f, indent=4)
#
# f.close()
#
#
# # function to add to JSON
# def write_json(new_data, filename='context.json'):
#     with open(filename, 'r+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["TennisRoster"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent=4)
#
#     # python object to be appended
#
#
# write_json(y2)
