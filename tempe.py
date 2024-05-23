readme_line = '''|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|\n|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|\n'''



# Writing table header, row separator, and table content to the readme1.md file
with open('readme2.md', 'w') as file:
    file.write('|   |   |   |   |   |   |   |   |   |   |\n')
    file.write('|---|---|---|---|---|---|---|---|---|---|\n')
    i=1
    while i<734:
        image_links=[f'![{img}.png](a_tulu_data/{img}.png)' for img in range(i,i+10)]
        numbers=[i for i in range(i,i+10)]
        file.write(readme_line.format(*image_links, *numbers))
        i+=10