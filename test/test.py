import tennisroster.context

ctx = tennisroster.context.Context("context.json")

ctx.load_input_data("samplelist.xlsx", 1)

ctx.create_matchups()
