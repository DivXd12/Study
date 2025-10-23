text = 'Protejarea libertății și a democrației El mai vorbește, în programul prezidențial, despre pericolele la adresa libertății sunt de ordin intern și de ordin extern și spune că libertatea românilor este amenințată de pericolul expansiunii sistemelor totalitare și dictatoriale în versiuni noi, mai înșelătoare decât totalitarismele brutale ale secolului trecut. Ciucă precizează că va veghea neobosit la libertatea românilor și a României și precizează că a făcut acest lucru ca militar, o va face și ca președinte. Strategia combaterii schimbărilor climatice Nicolae Ciucă mai propune promovarea unei strategii unitare pentru combaterea efectelor schimbărilor climatice și impactului acestora în societate. El mai spune că statultrebuie să acorde în mod egal protecție familiei indiferent de situația particulară în care se găsește, pentru că forța ei educativă și valorile pe care se bazează rămân aceleași, amintind că în țara noastră sunt multe familii monoparentale sau copii cu părinții plecați la lucru în străinătate.'

length = len(text)
tx1 = ''
tx2 = ''

if length % 2 == 0:
    tx1 = text[:length // 2].upper().replace(' ', '')
    tx2 = text[length // 2:][::-1]
    for ch in ['.', ',', '!', '?']:
        tx2 = tx2.replace(ch, '')
    tx2 = tx2[0].upper() + tx2[1:]
    print(tx1 + tx2)
else:
    tx1 = text[:length // 2 + 1].upper().replace(' ', '')
    tx2 = text[length // 2 + 1:][::-1]
    for ch in ['.', ',', '!', '?']:
        tx2 = tx2.replace(ch, '')
    tx2 = tx2[0].upper() + tx2[1:]
    print(tx1 + tx2)
