def get_criminal_conspiracy_triplets():
    triplets = [
        
        ("Section 120B IPC", "criminalizes", "Criminal Conspiracy"),
        ("Section 120B IPC", "defines_punishment_for", "Conspiracy to commit offences punishable with death/life/two years+"),
        ("Section 120B IPC", "is_cognizable_offence", True),
        ("Section 120B IPC", "is_bailable_offence", False),
        ("Section 120B IPC", "is_triable_by", "Court of Session"),
        ("Section 120B IPC", "requires", "Agreement to an illegal act"),
        ("Section 120B IPC", "liability_same_as_abettor", True),
        ("Section 120B IPC", "mens_rea_required", True),
        ("Criminal Conspiracy", "requires", "Agreement between two or more persons"),
        ("Criminal Conspiracy", "does_not_require", "Overt act (for major offences)"),
        ("Criminal Conspiracy", "can_be_proved_by", "Circumstantial evidence"),
        
        ("Section 120B IPC", "proven_by_evidence_type", "Eyewitness Testimony"),
        ("Section 120B IPC", "proven_by_evidence_type", "Corroboration"),
        ("Section 120B IPC", "proven_by_evidence_type", "Medical & Forensic Evidence (if offence involves harm)"),
        
        ("Section 120B IPC", "has_mens_rea_and_actus_reus_requirement", True),
        ("Mens Rea & Actus Reus", "required_for", "Criminal Liability in Conspiracy"),
        
        ("State v. Nalini (Rajiv Gandhi Assassination)", "interpreted_section", "Section 120B IPC"),
        ("State v. Nalini (Rajiv Gandhi Assassination)", "established_rule", "All conspirators equally liable"),
        ("State of Maharashtra v. Som Nath Thapa", "interpreted_section", "Section 120B IPC"),
        ("State of Maharashtra v. Som Nath Thapa", "established_rule", "Agreement itself is an offence"),
        ("Kehar Singh v. State (Indira Gandhi Assassination)", "interpreted_section", "Section 120B IPC"),
        ("Kehar Singh v. State (Indira Gandhi Assassination)", "established_rule", "Conspiracy may be proved by circumstantial evidence"),
    ]

    qa_chunks = [
        ("qa-120B-1", "What is the punishment under Section 120B IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-120B-2", "Is Section 120B a bailable offence?", "No, it is generally non-bailable."),
        ("qa-120B-3", "Is Section 120B a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-120B-4", "What is criminal conspiracy under Section 120A IPC?", "Criminal conspiracy means an agreement between two or more persons to commit an illegal act or a legal act by illegal means."),
        ("qa-120B-5", "Can mere agreement amount to criminal conspiracy under Section 120B?", "Yes, the act of agreeing itself constitutes criminal conspiracy even if no further act is done."),
        ("qa-120B-6", "Is criminal conspiracy under Section 120B IPC compoundable?", "No, conspiracy cases are not compoundable under law."),
        ("qa-120B-7", "Which court tries offences under Section 120B IPC?", "Session Courts generally try serious conspiracy cases, while Magistrate courts can try minor ones."),
        ("qa-120B-8", "Is intention required for conviction under Section 120B IPC?", "Yes, intention to commit an illegal act is necessary for conviction."),
        ("qa-120B-9", "Can a minor be prosecuted for criminal conspiracy?", "Yes, but if under 18, proceedings are under the Juvenile Justice Act."),
        ("qa-120B-10", "Can abetment of criminal conspiracy be punished?", "Yes, abetment is punishable under Sections 109/120B IPC."),
        ("qa-120B-11", "Is medical evidence required in criminal conspiracy cases?", "Medical evidence is not usually relevant unless the illegal act involves bodily harm."),
        ("qa-120B-12", "Can conviction under Section 120B IPC be appealed?", "Yes, the convicted individual may appeal in higher courts."),
        ("qa-120B-13", "Does conviction under Section 120B IPC affect government employment?", "Conviction for conspiracy may bar an individual from government service."),
        ("qa-120B-14", "Are companies or firms liable under Section 120B IPC?", "Yes, corporate entities can be held liable for criminal conspiracy if employees/directors are involved."),
        ("qa-120B-15", "Are criminal conspiracy cases triable without evidence of overt act?", "Yes, even without an overt act, evidence of agreement is sufficient for prosecution."),
        ("qa-120B-16", "What common defences exist against criminal conspiracy charges?", "Common defences include absence of agreement, lack of intention, or absence of illegal object."),
        ("qa-120B-17", "Is there any limitation period for trial under Section 120B IPC?", "Generally, there is no limitation for serious conspiracy offences."),
        ("qa-120B-18", "Are conspiracy cases under Section 120B IPC compoundable if parties settle?", "No, criminal conspiracy cases are non-compoundable and prosecuted even if parties settle."),
        ("qa-120B-19", "What recent trends are seen in criminal conspiracy cases under IPC?", "Recent trends include use of electronic communications as evidence and involvement of corporate entities."),
        ("qa-120B-20", "Is FIR necessary to begin criminal conspiracy prosecution?", "FIR is generally required to initiate investigation in criminal conspiracy offences under IPC."),
    ]

    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 120B IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))

    return triplets