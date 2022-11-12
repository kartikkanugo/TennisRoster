import pygraphviz as pgv
from datetime import datetime


class Flowchart:
    def __init__(self, context_list):
        self.context_list = context_list
        self.g = pgv.AGraph()
        self.g.node_attr["style"] = "filled"
        self.g.node_attr["shape"] = "circle"
        self.g.node_attr["fixedsize"] = "true"
        self.g.node_attr["fontcolor"] = "#ffffff"
        self.g.node_attr["fontsize"] = 17.0

    def create_round_flow_chart(self, round_num):
        dict_list = self.context_list[round_num]
        key_list = list(dict_list.keys())
        i = 0
        for teams, scores, sub_scores in zip(
            dict_list[key_list[0]], dict_list[key_list[1]], dict_list[key_list[2]]
        ):
            str_scores = (
                f"M{i}: {scores[0]}-{scores[1]} {sub_scores[0]}-{sub_scores[1]}"
            )
            self.g.add_edge(0, str_scores)
            self.g.add_edge(str_scores, f"L {teams[0]}")
            self.g.add_edge(str_scores, f"R {teams[1]}")

            n = self.g.get_node(str_scores)
            n.attr["fillcolor"] = f"#{i * 8:2x}0000"
            n.attr["height"] = f"{1.5}"
            n.attr["width"] = f"{1.5}"

            t0_n = self.g.get_node(f"L {teams[0]}")
            t0_n.attr["fillcolor"] = f"#00{i * 8:2x}00"
            t0_n.attr["height"] = f"{2}"
            t0_n.attr["width"] = f"{2}"

            t1_n = self.g.get_node(f"R {teams[1]}")
            t1_n.attr["fillcolor"] = f"#0000{i * 8:2x}"
            t1_n.attr["height"] = f"{2}"
            t1_n.attr["width"] = f"{2}"

            i = i + 1

        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M")
        round_data = dt_string + "_graph_" + str(round_num + 1) + ".png"
        self.g.draw(round_data, prog="circo")  # draw to png using circo layout

    def create_all_flow_charts(self):
        for i in range(len(self.context_list)):
            self.create_round_flow_chart(i)
