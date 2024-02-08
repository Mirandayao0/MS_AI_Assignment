
class ExtractGraph(object):
    # Please add comments along with your code.
    # key is head word; value stores next word and corresponding probability.
    graph = {}

    filepath = "./data/assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        self.graph = {}
        self.prob = {}

        with open("./data/assign1_sentences.txt", "r") as f:
            txt_all = f.readlines()
        self.construct_graph(txt_all)
        self.init_prob(show=False)
        return

    def construct_graph(self, txt_lines):
        # sort the content and construct the graph by the structure of dictionary
        for line in txt_lines:
            line = line.replace('\n', '')
            tokens = line.split(' ')
            for i, token in enumerate(tokens[:-1]):
                if not token in self.graph.keys():
                    self.graph[token] = {}
                next_token = tokens[i + 1]
                if not next_token in self.graph[token]:
                    self.graph[token][next_token] = 0
                self.graph[token][next_token] += 1

    def init_prob(self, show=False):
        # the part to init the prob graph
        for word in self.graph:
            if not word in self.prob:
                self.prob[word] = {}
            sum_num = sum([self.graph[word][next_word] for next_word in self.graph[word]])
            for next_word in self.graph[word]:
                self.prob[word][next_word] = self.graph[word][next_word] / sum_num
        if show:
            pp.pprint(self.prob)

    def getProb(self, head_word, tail_word):
        # the be called and return the probability
        # As the head_word/tail_word doesn't exist in the graph
        # return the probability of ZERO
        if not head_word in self.prob:
            return 0
        if not tail_word in self.prob[head_word]:
            return 0
        return self.prob[head_word][tail_word]


if __name__ == '__main__':
    graph = ExtractGraph()
