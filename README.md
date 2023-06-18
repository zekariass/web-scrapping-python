# Web Scrapping using python

This is a mini-scrapping script written in python to retrieve information on Medium blog posting site. Medium is a comprehensive
blogging website where various subject experts share their knowledge, skills and thoughts.

This code allows to get blog posts written related to coding and python.

## Used Languages and libraries
+ Python=3.11.2
+ beautifulsoup4==4.12.2
+ requests=2.31.0
+ Logging

```markdown
[   {   'blog_image': 'https://miro.medium.com/v2/resize:fill:224:224/1*kpksgzDd6qKP2h6GM7OVCA.png',
        'content': 'Visualising Geospatial Variations in Well Log Measurements '
                   'Within the Subsurface —  Interpreting the subsurface '
                   'requires understanding how geological and petrophysical '
                   'data varies across a region. This often involves dealing '
                   'with well log measurements and interpreted properties '
                   'scattered across the area, which leads to the challenge of '
                   'estimating the values between these measurements. One way '
                   'that we can estimate the values (or…',
        'posted_by': 'Andy McDonald',
        'read_time': '7 min read',
        'tag': 'Python',
        'title': 'Plotly and Python: Creating Interactive Heatmaps for '
                 'Petrophysical & Geological Data'},
    {   'blog_image': 'https://miro.medium.com/v2/resize:fill:224:224/1*Qiov_PZ_QvVZyDd3DFz5eQ.png',
        'content': 'Looking at the toolkit of useful mathematical techniques '
                   'involved in sketching curves —  With the advent of modern '
                   'technology, there is less and less need to sketch curves '
                   'by hand. …',
        'posted_by': 'Keith McNulty',
        'read_time': '8 min read',
        'tag': 'Python',
        'title': 'The Lost Art of Curve Sketching'},
        ...
]