"""
Created on Sun Dec 9

@author: Alejandra Licon
"""
import Filter
class FiltersContainer:

    def __init__(self):

        self.filterList = []

    def addFilter(self):
        self.filterList.append(currFilter)
        filterName = Filter.get("name")
        filterExpression = Filter.get("expression")
        currFilter = Field.Field(filterName,filterExpression)
        self.filterList.append(currFilter)

    def deleteFilter(filter):

