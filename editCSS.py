# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:02:50 2021

@author: sevda
"""

import cssutils

# Parse the stylesheet, replace color
parser = cssutils.parseFile('sentCsStyle.css')
for rule in parser.cssRules:
    try:
        if rule.selectorText == '#sent_3':
            #rule.style.backgroundColor = 'yellow'  # Replace background
            rule.style['background-color'] = 'pink'
            rule.style['color'] = 'purple' 
            rule.style['font-size'] = '12px'
            rule.style['font-style'] = 'italic'
            rule.style['font-family'] = '"Times New Roman", Times, serif'
            rule.style['font-weight'] = 'bold'
            
    except AttributeError as e:
        pass  # Ignore error if the rule does not have background

# Write to a new file
with open('style_new.css', 'wb') as f:
    f.write(parser.cssText)