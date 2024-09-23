
from pyscript import document
import json 
{
    "packages": ["arrr"]
}

def show(a):
    show=document.querySelector('#input32')
    button=document.querySelector('#show')

    if show.type=='password':
        show.type='text'
        button.src='show.png'
    else: 
        show.type='password'
        button.src='unshow.png'
