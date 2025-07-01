import subprocess

def check_spelling(text):
    '''Check spelling using aspell and return a set of misspelled words.'''
    p = subprocess.Popen(['aspell', 'list'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = p.communicate(text)
    return set(stdout.splitlines())