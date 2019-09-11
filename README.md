# Page Rank

### Setup

- `hadoop fs -put _movies/graph/adj_list /input` to place the adj list in the input folder.

### Commands

- `hadoop jar hadoop-streaming.jar -input /input/adj_list -output /out -mapper ./mapper.py -reducer reducer.py && hadoop fs -cat /out/part-00000` to rrun the Map Reduce algorithm. (Use _adj_ file for smaller tests)

- `hadoop jar hadoop-streaming.jar -input /out/part-00000 -output /maxs -mapper ./max_page_rank.py && hadoop fs -cat /maxs/part-00000`: to show the 20 top rresults

## 20 tops results:

After the first iteration:

```
1138    0.000126
1139    0.000126
1140    0.000126
1141    0.000126
1142    0.000126
1143    0.000126
1170    0.000123
1197    0.000126
1198    0.000126
1199    0.000126
12      0.000134
1200    0.000126
1209    0.000126
1210    0.000126
3701    0.000147
3966    0.000120
4       0.000120
524     0.000120
5322    0.000128
93      0.000183
```
