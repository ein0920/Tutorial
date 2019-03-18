

from xml.etree.ElementTree import iterparse


nums = [1,3,4,6,8,9]
for num in nums:
    filename = f'reading__Q{num}.xml'

    doc = iterparse(filename, ('start', 'end'))
    next(doc)

    i = 0
    opt = ['A. ', 'B. ', 'C. ', 'D. ']
    for event, elem in doc:
        if event == 'start' and elem.tag == 'questiontext':
            with open('question.txt', 'a') as f:
                text = elem.text.replace(' $pstart &lt;font face="Arial Unicode MS" size="10"&gt;', '')
                text = text.replace('&lt;/font&gt; $pend', '')
                text = text.replace('&lt;/i&gt;&lt;/font&gt;&lt;font face="Arial Unicode MS" size="10"&gt;? ', '')
                text = text.replace('&lt;/font&gt;&lt;font face="Arial Unicode MS" size="10"&gt;&lt;i&gt;', '')
                f.write(text + '\n')
        elif event == 'start' and elem.tag == 'optiontext':

            with open('question.txt', 'a') as f:
                text = elem.text.replace(' $pstart &lt;font face="Arial Unicode MS" size="10"&gt;', '')
                text = text.replace('&lt;/font&gt; $pend', '')
                f.write(opt[i] + text + '\n')
                i += 1

