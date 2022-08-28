import tennisroster.context

ctx = tennisroster.context.Context("context.json")

ctx.load_input_data("samplelist.xlsx", 1)

ctx.create_matchups()

vals = ctx.get_match_list(2)

print(vals)

points = [(3,2)] * len(vals)
sub_points = [(15, 30)]* len(vals)
win_list = [('W', 'L')]*len(vals)

ctx.update_scores(2, points, sub_points, win_list)


ctx.produce_flowchart(2)


ctx.generate_results(2)