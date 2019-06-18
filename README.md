# Scraping-BigData-companies-from-websites
Scraping BigData companies from websites is not much different than scraping Google scholar profiles. In this small examples I want to show you how to scrape specific names on a webpage, which are are/are not taged with a class. In the first example I wanted to scrape the names of companies on three pages of datanation.com. The pages only highlighted the names by putting them in bold, which is done by putting the text in the html file within a <strong> environment. The solution was easy.


First I created a list of the three pages. Then, I went through each list, read out the html content and search for <strong> environments. For each find, I then only extracted the text by using the .text command. see part one of code.
  
This allows to extract the inside of the <strong> environment. Next I wanted to extract the companies from a blog from Denny Britz a fellow German. Here the situation was a bit different. The company name I was looking for was in <a> environments, which had a class “external”. Using the findAll method I was able to extact only these parts and read out only the text.
The result is a list of companies, which all have something to do with BigData. Below is the list, which I got from the above Python scraping script and manual search. If you like web scraping in Python I would recommend the book “Web Scraping with Python” from Ryan Mitchell.
