import pygraphviz as pgv


class Flowchart:
    def __init__(self, context_list):
        self.context_list = context_list
        self.g = pgv.AGraph()
        self.g.node_attr["style"] = "filled"
        self.g.node_attr["shape"] = "circle"
        self.g.node_attr["fixedsize"] = "true"
        self.g.node_attr["fontcolor"] = "#FFFFFF"


    def create_round_flow_chart(self, round_num):
        dict_list = self.context_list[round_num]
        key_list = list(dict_list.keys())
        i = 0
        for teams, scores, sub_scores in zip(dict_list[key_list[0]], dict_list[key_list[1]], dict_list[key_list[2]]):

            str_scores = f"{scores[0]}.{sub_scores[0]} - {scores[1]}.{sub_scores[1]}"
            self.g.add_edge(0, str_scores)
            self.g.add_edge(str_scores, f"{teams[0]}")
            self.g.add_edge(str_scores, f"{teams[1]}")

            n = self.g.get_node(str_scores)
            n.attr["fillcolor"] = f"#{i * 16:2x}0000"
            n.attr["height"] = f"{i / len(dict_list[key_list[0]]) + 3}"
            n.attr["width"] = f"{i / len(dict_list[key_list[0]]) + 3}"
            i = i+1

        print(self.g.string())  # print to screen
        self.g.write("star.dot")  # write to simple.dot
        self.g.draw("star.png", prog="circo")  # draw to png using circo layout

    def create_all_flow_charts(self):
        pass
