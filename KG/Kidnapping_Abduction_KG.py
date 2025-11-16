def get_kidnapping_abduction_triplets():
    triplets = [
        # Statutes & Structure
        ("Section 359 IPC", "defines", "Kidnapping"),
        ("Section 359 IPC", "types", "From India / From lawful guardianship"),
        ("Section 362 IPC", "defines", "Abduction"),
        ("Section 362 IPC", "definition", "Inducement by force or deceit to move a person"),
        ("Section 359-374 IPC", "is_cognizable_offence", True),
        ("Section 359-374 IPC", "is_bailable_offence", False),
        ("Section 359-374 IPC", "is_triable_by", "Court of Session"),
        ("Section 359-374 IPC", "proven_by_evidence_type", "Witness Testimony"),
        ("Section 359-374 IPC", "proven_by_evidence_type", "Medical & Forensic Evidence"),
        ("Section 359-374 IPC", "mens_rea_actus_reus", "Both may be required, especially for aggravated forms"),
        # Doctrine
        ("Kidnapping/Abduction", "mens_rea", "Sometimes not required for basic kidnapping; required for abduction with intent"),
        # Precedents
        ("Sham Singh v. State of Haryana", "interpreted_section", "Section 364A IPC"),
        ("Sham Singh v. State of Haryana", "established_rule", "Ransom demand essential for conviction under Section 364A"),
        ("State v. Suresh", "interpreted_section", "Section 361/363 IPC"),
        ("State v. Suresh", "established_rule", "Consent of minor irrelevant for kidnapping"),
        ("Lallu Manjhi v. State of Jharkhand", "interpreted_section", "IPC 359-374"),
        ("Lallu Manjhi v. State of Jharkhand", "established_rule", "Distinction between kidnapping and abduction"),
    ]

    qa_chunks = [
        ("qa-359-374-1", "What is the punishment under Section 359-374 IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-359-374-2", "Is Section 359-374 a bailable offence?", "No, it is generally non-bailable."),
        ("qa-359-374-3", "Is Section 359-374 a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-359-374-4", "What is kidnapping as per Section 359 IPC?", "Kidnapping means taking away a person by force, deceit, or without consent from lawful guardianship."),
        ("qa-359-374-5", "What is abduction under Section 362 IPC?", "Abduction is the removal of a person by force or compulsion, usually for an illegal purpose."),
        ("qa-359-374-6", "Can kidnapping be compoundable under IPC?", "No, kidnapping offences under IPC are not compoundable."),
        ("qa-359-374-7", "What is the maximum punishment for kidnapping for ransom under Section 364A IPC?", "Maximum punishment is death penalty or life imprisonment and fine."),
        ("qa-359-374-8", "What is the difference between kidnapping and abduction under IPC?", "Kidnapping is an offence per se, requiring taking away without consent; abduction requires a criminal intent and is punishable only when done for specific purposes."),
        ("qa-359-374-9", "Is intention necessary for kidnapping under IPC?", "Intention is not required for the basic offence of kidnapping, but it is for aggravated forms like ransom or exploitation."),
        ("qa-359-374-10", "Can a minor be prosecuted for kidnapping or abduction?", "Yes, but proceedings are conducted under the Juvenile Justice Act if the accused is under 18."),
        ("qa-359-374-11", "Which court tries kidnapping/abduction cases under IPC?", "Usually tried by Sessions Court, especially for serious offences."),
        ("qa-359-374-12", "Can abetment of kidnapping/abduction be punished?", "Yes, abetment is punishable under relevant provisions such as Sections 107/108 IPC."),
        ("qa-359-374-13", "Does conviction for kidnapping affect government employment?", "Yes, conviction for kidnapping/abduction generally bars an individual from government service."),
        ("qa-359-374-14", "Can a conviction for kidnapping/abduction be appealed?", "Yes, a convicted person may appeal in High Court and Supreme Court."),
        ("qa-359-374-15", "Are there any common defences against kidnapping charges?", "Absence of intention, consent of the person taken, mistaken identity or lack of guardianship may be used as defence."),
        ("qa-359-374-16", "Is there any limitation period for trial under Section 359-374 IPC?", "No, serious offences such as kidnapping have no limitation period for prosecution."),
        ("qa-359-374-17", "Is medical evidence required in kidnapping/abduction cases?", "Medical evidence is relevant if there are physical injuries, otherwise witness testimonies are primary."),
        ("qa-359-374-18", "What recent trends are emerging in prosecution of kidnapping/abduction?", "Recent trends include use of electronic evidence, tracking mobile devices, and emphasis on quick rescue and rehabilitation of victims."),
        ("qa-359-374-19", "Are offences under IPC 359-374 compoundable if victim returns home?", "No, return of the victim does not compound the offence; prosecution proceeds as per law."),
        ("qa-359-374-20", "Is police complaint necessary for starting proceedings under Section 359-374 IPC?", "Yes, police complaint (FIR) initiates investigation in kidnapping/abduction cases under IPC."),
    ]

    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 359-374 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))
    return triplets

