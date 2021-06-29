# multiNBA

Suppose the task is given in our usual nomenclature:

```python
'''

subformula={ AP_id: [a,b,c]}

a: condition for AP_id to be True

b: desired probability

c: distance from landmark

'''

self.formula = '<>e1 && <> (e2 || e3)'
self.subformula = {1: ['(l4_2)',0.8,1.5],
                    2: ['(l8_1)',0.8,3], 
                    3: ['(l12_1)',0.8,5]
                    }
self.number_of_robots = 2
```

For this task the shortest path along the generated NBA will be fulfilled by (e1 && e2) || (e1 && e3)
This edge in the NBA is stored with the following information:
```python
buchi.buchi_graph.edges['T0_init', 'accept_all']= 
{'AP': '(e1 && e2) || (e1 && e3)', 
'AP_keys': ['1', '2', '1', '3'], 
'truth': {'l4_2': True, 'l8_1': True, 'l12_1': False}, 
'avoid': {0: [('l12', 5)], 1: []},
'all_truth': [{'l4_2': True, 'l8_1': True, 'l12_1': False}, {'l4_2': True, 'l12_1': True, 'l8_1': False}], 
'all_avoid': [{0: [('l12', 5)], 1: []}, {0: [('l8', 3)], 1: []}], 
'counter': 0, 
'avoid_self_loop': {0: [], 1: []}} 
```
Thus, currently, to enable the transition robot 2 must go to landmark 4 and robot 1 must go to landmark 8. The counter is 0 which means it pointing to first of the two possible truths (all_truth). 

When the user determines that this particular transition is not possible he can call any of the three functions to change the truth that enables the transition:
1)  ```python buchi.update_alternate_transition('T0_init', 'accept_all')```
        This will automatically increment the counter and the 'truth' will store the next possible truth. The function will return true if it successfully finds an alternate truth. Will return False if there are no more alternate truths available.
2) ```python buchi.previous_alternate_transition('T0_init', 'accept_all')```
        This will automatically decrement the counter and the 'truth' will store the next previous truth. The function will return true if it successfully finds an alternate truth. Will return False if there are no more alternate truths available.
3) ```python buchi.ctr_alternate_transition('T0_init', 'accept_all', counter)```
        This will automatically set the counter and the 'truth' as per the counter value specified. The function will return true if a valid counter value is provided.

In case none of the transitions are possible then the user can call "buchi.delete_transition('T0_init', 'accept_all')" function to delete that particular edge in the graph. 


Note:  line 98 in the buchi_parse code uses the distance mentioned in the task subformula. Thus if a different nomenclature is used for the task subformula, changes will be need to made in line 98 so that it points to the distance.
