from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def analize(request):
    if request.method=="GET":
        text = request.GET.get('text','no text here')
        
        UPPERCASE = request.GET.get('UPPERCASE','off')
        removepunctions = request.GET.get('removepunctions','off')
        charcount = request.GET.get('charcount','off')
        extraspaceremover = request.GET.get('extraspaceremover','off')

        if UPPERCASE == "on":
            analize_text = ""
            for char in text:
                analize_text =  analize_text + char.upper()
            context={'analize_text':analize_text,
                    'purpose':'UPPERCASE'}
            text = analize_text
        
        if removepunctions == "on":
            punctuation  = ''',".'[](){}:;?//*-+&*^%$#@!'''
            analize_text = ""
            for char in text:
                if char not in punctuation:
                    analize_text = analize_text + char
            context={'analize_text':analize_text,
                    'purpose':'RemovePunctions'}
            text = analize_text
            
        if extraspaceremover=="on":
            analize_text=""
            for index,char in  enumerate(text):
                if not(text[index]==" " and text[index+1]== " "):
                    analize_text = analize_text + char
                    context={'analize_text':analize_text,
                            'purpose':'Remove extra space'}
            text = analize_text
            
        if charcount == "on":
            analize_text = ""
            analize_text = len(text)
            context={'analize_text':analize_text,
                    'purpose':'charcount',
                    'char':'the total charcter in the text is :-'}
            text = analize_text

        if not(UPPERCASE=="on" and removepunctions=="on" and extraspaceremover=='on' and charcount=='on'):
            analize_text = text
            context ={'analize_text':analize_text,
                        'purpose':'Do Nothing'}
         
        return render (request,'analize.html',context)