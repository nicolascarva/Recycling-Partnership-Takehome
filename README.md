# Recycling-Partnership-Takehome


# Part 1
#########################################################

### Note: The .py file created is main.py and can be found on this repository: https://github.com/nicolascarva/Recycling-Partnership-Takehome.git

Instructions for running it:

1. Instantiate object with text to be searched (string or list) as input:
`input = Match('example text')`

2. Add desired pattern groups by running add_patterns method and using a dictionary with the pattern name as key and a list of the patterns as values. More pattern groups can be added as desired.

`pattern_group_1 = {'pat_1': ['ex', 'am'], 'pat_2': ['xt']}
pattern_group_2 = {'pat_3': ['foo']}
input.add_patterns(pattern_groups1)
input.add_patterns(pattern_groups2)`

3. To find matches run the match_patterns method with a list of the names of the desired pattern groups as input (if empty, default is 'all'):

`input.match_patterns(['pat_1'])`

4. If new text needs to be searched, a new object may be instantiated, or, to avoid having to add patterns again, run the change_text method with new text (string or list) as the input:

`input.change_text(['new', 'text'])` or 
`input.change_text('new text')`


#########################################################

# Part 2

The test code can be found in the `test_class.py` file. 
To run it, execute `python -m pytest` from the command line in the environment.

#########################################################

# Part 3

The exploratory data analysis was done on the original `takehome.ipynb` notebook.
The EDA consisted mainly of:
- text cleanup
- Document Term Matrix (DTM) and word frequency
- Bag of Words (BoW) and Latent Dirichlet Allocation (LDA)

#########################################################