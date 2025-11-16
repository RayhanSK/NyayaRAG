def get_assault_triplets():
    triplets = [
        ("Section 351 IPC", "defines", "Assault"),
        ("Section 352 IPC", "prescribes_punishment_for", "Assault"),
        ("Section 351/352 IPC", "is_cognizable_offence", True),
        ("Section 351/352 IPC", "is_bailable_offence", False),
        ("Section 351/352 IPC", "is_triable_by", "Sessions Court"),
        
        ("Assault case", "proven_by_evidence_type", "Eyewitness Testimony"),
        ("Assault case", "proven_by_evidence_type", "Medical & Forensic Evidence"),
        ("Assault case", "requires", "Mens Rea & Actus Reus"),
        ("Mens Rea & Actus Reus", "required_for", "Criminal Liability in Assault"),

        ("Rupan Deol Bajaj v. KPS Gill", "interpreted_section", "Section 352 IPC"),
        ("Rupan Deol Bajaj v. KPS Gill", "established_rule", "Assault includes any act causing apprehension"),
        ("State v. Anil Sharma", "interpreted_section", "Section 352 IPC"),
        ("State v. Anil Sharma", "established_rule", "Grave provocation lowers punishment for assault"),
        ("Santokh Singh v. State", "interpreted_section", "Section 352 IPC"),
        ("Santokh Singh v. State", "established_rule", "Assault without injury is Section 352 IPC"),
    ]

    qa_chunks = [
        ("qa-351/352-1", "What is the punishment under Section 351/352 IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-351/352-2", "Is Section 351/352 a bailable offence?", "No, it is generally non-bailable."),
        ("qa-351/352-3", "Is Section 351/352 a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-351/352-4", "What is the legal definition of assault under Section 351 IPC?", "Assault is any gesture or preparation to use criminal force, intentionally causing apprehension of harm in another person."),
        ("qa-351/352-5", "What is criminal force under Section 352 IPC?", "Criminal force is using force intentionally without consent to commit an offence or cause injury, fear, or annoyance."),
        ("qa-351/352-6", "Is assault under Section 351/352 IPC compoundable?", "Yes, assault and use of criminal force under Sections 351/352 are typically compoundable with court permission."),
        ("qa-351/352-7", "Which court tries offences under Section 351/352 IPC?", "Usually tried by Magistrate courts as these are less serious offences."),
        ("qa-351/352-8", "Can assault under Section 351 IPC occur without any physical contact?", "Yes, assault involves an act or gesture causing apprehension of harm—even without physical contact."),
        ("qa-351/352-9", "Is intention necessary for conviction under Section 352 IPC?", "Yes, intention to use force is a necessary ingredient for conviction."),
        ("qa-351/352-10", "What is the maximum punishment for assault under Section 352 IPC?", "Maximum punishment is imprisonment up to 3 months, or fine up to 500 rupees, or both."),
        ("qa-351/352-11", "Can minors be prosecuted under Section 351/352 IPC?", "Yes, but juvenile offenders are dealt with under the Juvenile Justice Act."),
        ("qa-351/352-12", "Are there any defences to assault under Section 351/352 IPC?", "Common defences include lack of intention, self-defence, consent, or act done without criminal force."),
        ("qa-351/352-13", "Does conviction under Section 351/352 affect government employment?", "It may affect government employment, depending on the nature and seriousness of the conviction."),
        ("qa-351/352-14", "Can a conviction under Section 351/352 IPC be appealed?", "Yes, convicts may appeal the decision in higher courts."),
        ("qa-351/352-15", "Is there any limitation period for trial under Section 351/352 IPC?", "Yes, generally 1 year for minor offences."),
        ("qa-351/352-16", "Is medical evidence required in Section 351/352 IPC cases?", "Medical evidence is needed if there are physical injuries due to alleged criminal force."),
        ("qa-351/352-17", "What recent trends have emerged in assault cases under IPC?", "Recent trends include reliance on CCTV footage, eyewitness accounts, and swift trials for summary offences."),
        ("qa-351/352-18", "Can abetment of assault under Section 351/352 IPC be punished?", "Yes, abetment is punishable under relevant provisions, like Section 109 IPC."),
        ("qa-351/352-19", "Is public servant immunity available under Section 351/352 IPC?", "If the act was done in good faith while performing official duty, public servants may invoke immunity under IPC."),
        ("qa-351/352-20", "Is a complaint mandatory for starting proceedings under Section 351/352 IPC?", "A complaint is not mandatory; police can act on their own for cognizable assault offences."),
    ]

    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 351/352 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))

    return triplets
