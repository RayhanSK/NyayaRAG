def get_murder_triplets():
    triplets = [
        # Statute & Structure
        ("Section 302 IPC", "prescribes_punishment_for", "Murder"),
        ("Section 302 IPC", "punishment", "Death or life imprisonment and fine"),
        ("Section 302 IPC", "is_cognizable_offence", True),
        ("Section 302 IPC", "is_bailable_offence", False),
        ("Section 302 IPC", "is_triable_by", "Court of Session"),
        ("Section 302 IPC", "requires", "Intention or knowledge to cause death"),
        ("Section 302 IPC", "mens_rea", "Intention/knowledge"),
        ("Section 302 IPC", "actus_reus", "Act causing death"),
        ("Section 302 IPC", "compoundable", False),
        # Doctrine & Ingredients
        ("Murder", "ingredients", "mens rea + actus reus causing death"),
        # Precedents
        ("K.M. Nanavati v. State of Maharashtra", "interpreted_section", "Section 302 IPC"),
        ("K.M. Nanavati v. State of Maharashtra", "established_rule", "Heat of passion may reduce offence"),
        ("State of Rajasthan v. Kashi Ram", "interpreted_section", "Section 302 IPC"),
        ("State of Rajasthan v. Kashi Ram", "established_rule", "Circumstantial chain of evidence must be complete"),
        ("Bachan Singh v. State of Punjab", "interpreted_section", "Section 302 IPC"),
        ("Bachan Singh v. State of Punjab", "established_rule", "Death penalty only in rarest of rare cases"),
    ]

    qa_chunks = [
        ("qa-302-1", "What is the punishment under Section 302 IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-302-2", "Is Section 302 a bailable offence?", "No, it is generally non-bailable."),
        ("qa-302-3", "Is Section 302 a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-302-4", "What is the minimum punishment for Section 302 IPC?", "The minimum punishment is life imprisonment; death penalty is also possible depending on the case."),
        ("qa-302-5", "What is the maximum punishment under Section 302 IPC?", "The maximum punishment is the death penalty."),
        ("qa-302-6", "Is Section 302 IPC compoundable?", "No, offences under Section 302 are not compoundable in the eyes of law."),
        ("qa-302-7", "Do all murders result in the death penalty under Section 302?", "No, the death penalty is given only in the 'rarest of rare' cases; otherwise, life imprisonment is awarded."),
        ("qa-302-8", "What are the essential ingredients of murder under Section 302 IPC?", "There must be an act of causing death, intention or knowledge to cause death, and the act must not fall under exceptions of Section 300."),
        ("qa-302-9", "Does Section 302 IPC require intention to kill?", "Yes, intention or knowledge that the act is likely to cause death is necessary for conviction."),
        ("qa-302-10", "Can a minor be charged under Section 302 IPC?", "Yes, but if the accused is under 18 years, provisions of the Juvenile Justice Act apply for trial and sentencing."),
        ("qa-302-11", "What is the difference between Section 300 and Section 302 IPC?", "Section 300 defines murder; Section 302 prescribes the punishment for murder."),
        ("qa-302-12", "Can Section 302 IPC be invoked for attempt to murder?", "No, attempt to murder is covered under Section 307 IPC, not Section 302."),
        ("qa-302-13", "Does a life sentence under Section 302 mean imprisonment for the convict's entire life?", "Yes, unless remitted or commuted as per law by appropriate government authorities; generally, life imprisonment means remainder of natural life."),
        ("qa-302-14", "Can Section 302 IPC cases be tried by a Magistrate?", "No, Section 302 offences are triable only by a Court of Session due to their seriousness."),
        ("qa-302-15", "Are medical reports necessary in Section 302 IPC prosecutions?", "Medical reports and post-mortem examination are crucial evidence to establish cause of death in murder cases."),
        ("qa-302-16", "What are some common defences against a charge of murder under Section 302?", "Common defences include absence of intention, grave and sudden provocation, private defence, alibi, unsound mind, and benefit of doubt due to insufficient evidence."),
        ("qa-302-17", "What is the limitation period for trial under Section 302 IPC?", "There is no limitation period for murder prosecutions; the case can be tried at any time after the commission of the offence."),
        ("qa-302-18", "Is abetment of murder punishable under Section 302 IPC?", "Abetment is punished under Section 109 or 120B IPC in combination with Section 302, not under Section 302 alone."),
        ("qa-302-19", "Do Section 302 IPC convictions affect government employment?", "Yes, conviction for murder (Section 302) generally disqualifies a person from government service."),
        ("qa-302-20", "Can a conviction under Section 302 IPC be appealed?", "Yes, a person convicted under Section 302 IPC can appeal to the High Court and subsequently to the Supreme Court."),
    ]

    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 302 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))
    return triplets
