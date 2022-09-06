from utils import *



def translate_file(file_input:str,file_output:str,source:str,target:str):
    # read file
    data = read_file(file_input)
    
    pattern = '<nghia_text>(.*?)</nghia_text>'
    L_sentence = regex_many_value(pattern, data)

    # translate each line
    for sentence in L_sentence:
        sentence_translated = translate(sentence,source,target)
        data = data.replace(
            f'<nghia_text>{sentence}</nghia_text>',
            f'<nghia_text>{sentence_translated}</nghia_text>',

        )
        
    # replace nonsense tag
    data = data.replace(
        '<nghia_text>',''
    ).replace(
        '</nghia_text>',''
    )

    # write file
    write_file(file_output,data)

if __name__ =="__main__":
    file_input = "input.html"
    file_output = "output.html"
    source = 'en'
    target = 'vi'
    translate_file(file_input,file_output,source,target)