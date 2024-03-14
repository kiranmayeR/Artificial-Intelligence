symptom(amit,fever).
    symptom(amit,rash).
    symptom(amit,headache).
    symptom(amit,runny_nose).

    symptom(kaushal,chills).
    symptom(kaushal,fever).
    symptom(kaushal,hedache).

    symptom(dipen,runny_nose).
    symptom(dipen,rash).
    symptom(dipen,flu).


    hypothesis(Patient,measels):-
        symptom(Patient,fever),
        symptom(Patient,cough),
        symptom(Patient,conjunctivitis),
        symptom(Patient,rash),
        write('Eat Salad').

    hypothesis(Patient,german_measles) :-
        symptom(Patient,fever),
        symptom(Patient,headache),
        symptom(Patient,runny_nose),
        symptom(Patient,rash),
        write('Avoid Oily Food').

    hypothesis(Patient,flu) :-
% Facts: Symptoms and Conditions
symptom(fever, flu).
symptom(cough, flu).
symptom(cough, cold).
symptom(headache, flu).
symptom(sore_throat, cold).
symptom(runny_nose, cold).
symptom(runny_nose, allergy).

% Rule: Diagnosis based on Symptoms
diagnose_patient(Symptoms) :-
    member(Symptom, Symptoms),
    symptom(Symptom, Diagnosis),
    format('The patient may have ~w.~n', [Diagnosis]).

% Interactive Interface
patient_diagnosis :-
    write('Enter symptoms (comma-separated): '),
    read(Symptoms),
    diagnose_patient(Symptoms).

% Example Usage:
% Run the query patient_diagnosis. and input symptoms when prompted.
