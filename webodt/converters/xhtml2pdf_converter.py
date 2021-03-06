#coding:utf-8
from webodt.converters import ConverterError
from webodt.helpers import guess_format_and_filename
try:
    from xhtml2pdf import pisa
except ImportError:
    print u'For use this converter, please, install xhtml2pdf'
from webodt import Document


class XHTML2PDFConverter(object):

    WEBODT_DEFAULT_FORMAT = 'pdf'

    def convert(self, document, format=None, output_filename=None, delete_on_close=True):
        if format != 'pdf':
            raise ConverterError, u'Not supported format %s by xhtml2pdf' % format
        output_filename, format = guess_format_and_filename(output_filename, format)
        input_file = document
        input_filename = document.name
        output_file = open(output_filename, 'wb')

        result = pisa.pisaDocument(
            input_file, output_file, path=input_filename, encoding='UTF-8',
        )

        output_file.close()

        if result.err:
            err_msg = 'Error rendering %s: %s' % (input_filename, result.err)
            raise ConverterError, err_msg
        fd = Document(output_filename, mode='rb', delete_on_close=delete_on_close)
        return fd
