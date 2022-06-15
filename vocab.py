
import random, copy

import numpy

from flask import Flask, render_template, request

import string

 

app = Flask(__name__)

 

questions  = {"Q. Hoard -":[" (a) Destroy" , " (b) Hide" , " (c) Store" , " (d) Divide" , " (c) Store"],

            "Q. Destitution -":[" (a) Adequacy" , " (b) Poverty" , " (c) Humility" , " (d) Moderation" , " (b) Poverty"],

             "Q. Desultory -" :[" (a) Obedient" , " (b) Punctual" , " (c) Regular" , " (d) Aimless" , " (d) Aimless"],

              "Q. Plush -" :[" (a) Comforting" , " (b) Luxurious" , " (c) Tasty" , " (d) Delicious" , " (b) Luxurious"],

              "Q. Competence -" :[" (a) Fleuncy" , " (b) Competition" , " (c) Ability" , " (d) Compensation" , " (c) Ability"],

              "Q. Infernal -" :[" (a) Exacting" , " (b) Angelic" , " (c) Devilish" , " (d) Damaging" , " (c) Devilish"],

              "Q. Baffle -" :[" (a) Insult" , " (b) Defame" , " (c) Hunger" , " (d) Frustrate" , " (d) Frustrate"],

              "Q. Deft -" :[" (a) Skillful" , " (b) Vigorous" , " (c) Clumsy" , " (d) Deceitful" , " (a) Skillful"],

              "Q. Eradicate -" :[" (a) Complicate" , " (b) Indicate" , " (c) Dedicate" , " (d) Eliminate" ," (d) Eliminate"],

              "Q. Brace -" :[" (a) Waste" , " (b) Grip" , " (c) Define" , " (d) Confine" , " (b) Grip"],

              "Q. Advice -" :[" (a) Council" , " (b) Counsel" , " (c) Practice" , " (d) Proposal" , " (b) Counsel"],

              "Q. Miserable -" :[" (a) Object" , " (b) Obstruct" , " (c) Abject" , " (d) Abstract" , " (c) Abject"],

              "Q. Quote -" :[" (a) Sight" , " (b) Sigh" , " (c) Sue" , " (d) Cite" , " (d) Cite"],

              "Q. Harmony -" :[" (a) Cemetery" , " (b) Ceremony" , " (c) Symmetry" , " (d) Hierarchy" , " (c) Symmetry"],

              "Q. Unlawful -" :[" (a) Elicit" , " (b) Draw" , " (c) Litigation" , " (d) Illicit" , " (d) Illicit"],

              "Q. Haughty -" :[" (a) Imperial" , " (b) Arrogant" , " (c) Adamant" , " (d) Empire" , " (b) Arrogant"],

              "Q. Wise -" :[" (a) Momentous" , " (b) Pragmatic" , " (c) Judicious" , " (d) Delay" , " (c) Judicious"],

              "Q. Loquacious -" :[" (a) Victorian" , " (b) Bombastic" , " (c) Verbose" , " (d) Ambiguous" , " (c) Verbose"],

              "Q. Courageous -" :[" (a) Fickle" , " (b) Insipid" , " (c) Timorous" , " (d) Fearless" , " (d) Fearless"],

              "Q. Watchfulness -" :[" (a) Supervision" , " (b) Custody" , " (c) Superintendence" , " (d) Vigil" , " (d) Vigil"],

              "Q. Attachment -" :[" (a) Affinity" , " (b) Influence" , " (c) Causation" , " (d) Appendage" , " (a) Affinity"],

              "Q. Weary -" :[" (a) Sad" , " (b) Fatigued" , " (c) Sentimental" , " (d) Emotional" , " (b) Fatigued"],

              "Q. Bequest -" :[" (a) Parsimony" , " (b) Matrimony" , " (c) Heritage" , " (d) Patrimony" , " (c) Heritage"],

              "Q. Guillible -" :[" (a) Credible" , " (b) Believable" , " (c) Credulous" , " (d) Fallible" , " (c) Credulous"],

              "Q. Bravery -" :[" (a) Onslaught" , " (b) Arrogant" , " (c) Fortitude" , " (d) Nepotism" , " (c) Fortitude"],

              "Q. Kind -" :[" (a) Nice" , " (b) Wild" , " (c)Funny" , " (d)Best" , " (a) Nice"],

              "Q. Difficult-" :[" (a) Hard" , " (b) Simple" , " (c) Easy" , " (d) Short" , " (a) Hard"],

              "Q. Glad -" :[" (a) Broken" , " (b) Happy" , " (c) Open" , " (d) Round" , " (b) Happy"],

              "Q. Big -" :[" (a) Large" , " (b) Heavy" , " (c) Hard" , " (d) Short" , " (a) Large"],

              "Q. Fast -" :[" (a) Clear" , " (b) Clean" , " (c) Quick" , " (d) Easy" , " (c) Quick"],

              "Q. Noisy -" :[" (a) First" , " (b) Loud" , " (c) Afraid" , " (d) Small" , " (b) Loud"],

              "Q. Scared -" :[" (a) Happy" , " (b) Sad" , " (c) Angry" , " (d) Afraid" , " (d) Afraid"],

              "Q. Smart -" :[" (a) Dumb" , " (b) Wide" , " (c) Intelligent" , " (d) Old" , " (c) Intelligent"],

              "Q. Rich -" :[" (a)Correct" , " (b) Different" , " (c) Wealthy" , " (d) Good" , " (c)"],

              "Q. Weird -" :[" (a) Strange" , " (b) Great" , " (c) Calm" , " (d) Typical" , " (a) Wealthy"],

              "Q. Sure -" :[" (a) Likely" , " (b) Doubtful" , " (c) Certain" , " (d) Smart" , " (a) Likely"],

              "Q. Fostering -" :[" (a) Safeguarding" , " (b) Neglecting" , " (c) Ignoring" , " (d) Nurturing" , " (d) Nurturing"],

              "Q. Propel -" :[" (a) Drive" , " (b) Jettison" , " (c) Burst" , " (d) Acclimatize" , " (a) Safeguarding"],

              "Q. Massive -" :[" (a) Lump sum" , " (b) Gaping" , " (c) Huge" , " (d) Strong" , " (c) Huge"],

              "Q. Stumbling Block -" :[" (a) Argument" , " (b) Frustration" , " (c) Advantage" , " (d) Hurdle" , " (d) Hurdle"],

              "Q. Defer -" :[" (a) Indifferent" , " (b) Defy" , " (c) Differ" , " (d) Postpone" , " (d) Postpone"],

              "Q. Adversity -" :[" (a) Failure" , " (b) Helplessness" , " (c) Misfortune" , " (d) Crisis" , " (c) Misfortune"],

              "Q. Fake -" :[" (a) Original" , " (b) Imitation" , " (c) Trustworthy" , " (d) Loyal" , " (b) Imitation"],

              "Q. Indict -" :[" (a) Condemn" , " (b) Reprimand" , " (c) Accuse" , " (d) Allege" , " (c) Accuse"],

              "Q. Stringnet -" :[" (a) Dry" , " (b) Strained" , " (c) Rigorous" , " (d) Shrill" , " (c) Rigorous"],

              "Q. Lament -" :[" (a) Complain" , " (b) Comment" , " (c) Condone" , " (d) Console" , " (a) Complain"],

              "Q. Garnish -" :[" (a) Paint" , " (b) Garner" , " (c) Adorn" , " (d) Abuse" , " (c) Adorn"],

              "Q. Mendacious -" :[" (a) Full of Confidence" , " (b) False" , " (c) Encouraging" , " (d) Provocative" , " (b) False"],

              "Q. Garruilty -" :[" (a) Credulity" , " (b) Senility" , " (c) Loquaciousness" , " (d) Speciousness" , " (c) Loquaciousness"],

              "Q. Morose -" :[" (a) Annoyed" , " (b) Gloomy" , " (c) Moody" , " (d) Displeased" , " (b) Gloomy"],

              "Q. Voracious -" :[" (a) Truthful" , " (b) Gluttonous" , " (c) Funny" , " (d) Venturous" , " (b) Gluttonous"], 

            }

 

r=list(questions.items())

 

numpy.random.shuffle(r)

a=dict(r)

k2=dict.keys(a) #dict of keys

k=list(k2) #list of keys

v2=dict.values(a) #dict of values

v=list(v2) #list of values

ans1=v[0][4]

ans2=v[1][4]

ans3=v[2][4]

ans4=v[3][4]

ans5=v[4][4]

ans6=v[5][4]

ans7=v[6][4]

ans8=v[7][4]

ans9=v[8][4]

ans10=v[9][4]

 

@app.route('/')

def vocabulary():

    val1=v[0]

    op1=val1[0]

    op2=val1[1]

    op3=val1[2]

    op4=val1[3]

    val2=v[1]

    op5=val2[0]

    op6=val2[1]

    op7=val2[2]

    op8=val2[3]

    val3=v[2]

    op9=val3[0]

    op10=val3[1]

    op11=val3[2]

    op12=val3[3]

   val4=v[3]

    op13=val4[0]

    op14=val4[1]

    op15=val4[2]

    op16=val4[3]

    val5=v[4]

    op17=val5[0]

    op18=val5[1]

    op19=val5[2]

    op20=val5[3]

 

    val6=v[5]

    op21=val6[0]

    op22=val6[1]

    op23=val6[2]

    op24=val6[3]

    val7=v[6]

    op25=val7[0]

    op26=val7[1]

    op27=val7[2]

    op28=val7[3]

    val8=v[7]

    op29=val8[0]

    op30=val8[1]

    op31=val8[2]

    op32=val8[3]

    val9=v[8]

    op33=val9[0]

    op34=val9[1]

    op35=val9[2]

    op36=val9[3]

    val10=v[9]

    op37=val10[0]

    op38=val10[1]

    op39=val10[2]

    op40=val10[3]   

    

 

    return render_template('vocab.html',k=k, v=v,op1=op1,op2=op2,op3=op3,op4=op4,op5=op5,op6=op6,op7=op7,op8=op8,op9=op9,op10=op10,

    op11=op11,op12=op12,op13=op13,op14=op14,op15=op15,op16=op16,op17=op17,op18=op18,op19=op19,op20=op20,op21=op21,op22=op22,op23=op23,

    op24=op24,op25=op25,op26=op26,op27=op27,op28=op28,op29=op29,op30=op30,op31=op31,op32=op32,op33=op33,op34=op34,op35=op35,op36=op36,

    op37=op37,op38=op38,op39=op39,op40=op40,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4,ans5=ans5,ans6=ans6,ans7=ans7,ans8=ans8,ans9=ans9,ans10=ans10)

 

@app.route('/vocabulary', methods = ["POST", "GET"])

 

def vocabulary_answers() :

 

    score = 0

    s1=s2=s3=s4=s5=s6=s7=s8=s9=s10=0

 

    oplist1=str(request.form['oplist1'])

    if oplist1==ans1:

        s1=s1+2

   

    oplist2=str(request.form['oplist2'])

    if oplist2==ans2:

        s2=s2+2

 

    oplist3=str(request.form['oplist3'])

    if oplist3==ans3:

        s3=s3+2

   

    oplist4=str(request.form['oplist4'])

    if oplist4==ans4:

        s4=s4+2

   

    oplist5=str(request.form['oplist5'])

    if oplist5==ans5:

        s5=s5+2

 

    oplist6=str(request.form['oplist6'])

    if oplist6==ans6:

        s6=s6+2

 

    oplist7=str(request.form['oplist7'])

    if oplist7==ans7:

        s7=s7+2

 

    oplist8=str(request.form['oplist8'])

    if oplist8==ans8:

        s8=s8+2

 

    oplist9=str(request.form['oplist9'])

    if oplist9==ans9:

        s9=s9+2

       

    oplist10=str(request.form['oplist10'])

    if oplist10==ans10:

        s10=s10+2

 

    score=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10

 

    return render_template('result.html', n=score)

 

if __name__=="__main__":

 

    app.run(debug=True)