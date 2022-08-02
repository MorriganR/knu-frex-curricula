import os
import markdown
import pdfkit

testHtmlFileName = './temp/test.html'
testPdfFileName = './temp/test.pdf'

testStyle = """<style>
table {
    border-collapse: collapse;
}
table, th, td {
   border: 1px solid black;
}
</style>"""

pdfKitOptions = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '1.00in',
    'encoding': "UTF-8"
}

try:
    os.remove(testHtmlFileName)
    os.remove(testPdfFileName)
except OSError:
    pass

testHtml = open(testHtmlFileName, 'a', encoding='utf-8')
# testPdf = open(testPdfFileName, 'a', encoding='utf-8')

# set html charset
testHtml.write("""<meta http-equiv="Content-type" content="text/html; charset=utf-8" />""")
testHtml.write(testStyle)

coursesDetaisPath = './Bachalor/Computer Engineering/details'
coursesList = os.listdir(coursesDetaisPath)
coursesList.sort()
# print('\n'.join(coursesList))
for course in coursesList:
    # courseDetailFileName = coursesDetaisPath + '/' + course + '/README.md'
    courseDetailUaFileName = coursesDetaisPath + '/' + course + '/README_UA.md'
    if os.stat(courseDetailUaFileName).st_size > 42:
        print(courseDetailUaFileName + ' - ' + str(os.stat(courseDetailUaFileName).st_size))
        # courseDetail = open(courseDetailFileName, 'r', encoding='utf-8')
        courseDetailUa = open(courseDetailUaFileName, 'r', encoding='utf-8')
        testHtml.write(markdown.markdown(courseDetailUa.read(), extensions=['tables'], output_format='html'))
        # courseDetail.close()
        courseDetailUa.close()


# testPdf.write("test to Pdf\n")

testHtml.close()
# testPdf.close()

pdfkit.from_file(testHtmlFileName, testPdfFileName, options=pdfKitOptions)