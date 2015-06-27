#!/usr/bin/python
# coding: utf-8
import sys
from firebase import firebase

url = 'https://xxx.firebaseio.com' # insert Firebase Data URL
firebase = firebase.FirebaseApplication(url, None)

morse_code_lookup = {
    "..-..-":    "σ ﾟ∀ ﾟ) ﾟ∀ﾟ)σ ",
    ".-.":    "(╯‵□′)╯︵┴─┴",
    ".-.-": "ლ(・ω・ლ)",
    "--": "ಠ౪ಠ",
    "..-": "ヾ(●゜▽゜●)♡",
    "-..": "(☉д⊙)",
    "...-": "╮(╯∀╰)╭",
    "--..": "٩(ŏ﹏ŏ、)۶",
    "-.-.": "｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡",
    ".--.": "（´◔ ₃ ◔`)",
    "..--": "(✧≖‿ゝ≖)",
    "---": "(╥﹏╥)",
    "--...--...":    "ʕ•̫͡•ʔ→ʕ•̫͡•̫͡•ʔ→ʕ•̫͡•=•̫͡•ʔ→ʕ•̫͡•ʔʕ•̫͡•ʔ→ʕ•̫͡•̫͡•ʔ ʕ•̫͡•̫͡•ʔ"
}

def try_decode(bit_string, roundId):
    if bit_string in morse_code_lookup.keys():
        data = firebase.get('/morse', roundId)
        s = morse_code_lookup[bit_string]
        data['input'] = data['input'].encode("utf-8")
        data['input'] += s
        firebase.patch('/morse/' + roundId, {'input':data['input']})
        data = firebase.get('/morse', roundId)
        sys.stdout.write(morse_code_lookup[bit_string])
        sys.stdout.flush()
