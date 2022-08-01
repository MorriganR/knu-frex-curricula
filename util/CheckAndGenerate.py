import os

testDocFileName = './temp/test.doc'
testPdfFileName = './temp/test.pdf'

try:
    os.remove(testDocFileName)
    os.remove(testPdfFileName)
except OSError:
    pass

testDoc = open(testDocFileName, 'a', encoding='utf-8')
testPdf = open(testPdfFileName, 'a', encoding='utf-8')

coursesDetaisPath = './Bachalor/Computer Engineering/details'
coursesList = os.listdir(coursesDetaisPath)
# print('\n'.join(coursesList))
for course in coursesList:
    courseDetailFileName = coursesDetaisPath + '/' + course + '/README.md'
    courseDetailUaFileName = coursesDetaisPath + '/' + course + '/README_UA.md'
    if os.stat(courseDetailUaFileName).st_size > 42:
        print(courseDetailUaFileName + ' - ' + str(os.stat(courseDetailUaFileName).st_size))
        courseDetail = open(courseDetailFileName, 'r', encoding='utf-8')
        courseDetailUa = open(courseDetailUaFileName, 'r', encoding='utf-8')
        courseDetail.close()
        courseDetailUa.close()

testDoc.write("test to Doc\n")
testPdf.write("test to Pdf\n")

testDoc.close()
testPdf.close()