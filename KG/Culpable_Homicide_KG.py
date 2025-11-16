def get_culpable_homicide_triplets():
    triplets = [
        # Statutes & Structure
        ("Section 299 IPC", "defines", "Culpable Homicide"),
        ("Section 299 IPC", "requires", "Intention or knowledge causing death"),
        ("Section 300 IPC", "defines", "When Culpable Homicide is Murder"),
        ("Section 299/300 IPC", "is_cognizable_offence", True),
        ("Section 299/300 IPC", "is_bailable_offence", False),
        ("Section 299/300 IPC", "is_triable_by", "Court of Session"),
        ("Section 299/300 IPC", "has_mens_rea_actus_reus", True),
        ("Culpable Homicide", "may_be", "Murder"),
        ("Murder", "is", "Aggravated form of Culpable Homicide"),
        # Evidence & Doctrine
        ("Section 299/300 IPC", "proven_by_evidence_type", "Witness Testimony"),
        ("Section 299/300 IPC", "proven_by_evidence_type", "Medical & Forensic Evidence"),
        ("Section 299/300 IPC", "proven_by_evidence_type", "Corroboration"),
        ("Section 299/300 IPC", "mens_rea", "Required"),
        ("Section 299/300 IPC", "actus_reus", "Required"),
        # Precedents
        ("Virsa Singh v. State of Punjab", "interpreted_section", "Section 300 IPC"),
        ("Virsa Singh v. State of Punjab", "established_rule", "Single blow can amount to murder if injury sufficient to cause death"),
        ("Reg v. Govinda", "interpreted_section", "Section 299 & 300 IPC"),
        ("Reg v. Govinda", "established_rule", "Distinction between culpable homicide and murder"),
        ("State of Andhra Pradesh v. Rayavarapu Punnayya", "interpreted_section", "Section 299 & 300 IPC"),
        ("State of Andhra Pradesh v. Rayavarapu Punnayya", "established_rule", "Murder is aggravated form of culpable homicide"),
    ]

    qa_chunks = [
        ("qa-299/300-1", "What is the punishment under Section 299/300 IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-299/300-2", "Is Section 299/300 a bailable offence?", "No, it is generally non-bailable."),
        ("qa-299/300-3", "Is Section 299/300 a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-299/300-4", "What is the definition of culpable homicide under Section 299 IPC?", "Culpable homicide means causing death by doing an act with intention or knowledge that death is likely to result."),
        ("qa-299/300-5", "How is murder differentiated from culpable homicide in the IPC?", "All murder is culpable homicide but only the most aggravated forms of culpable homicide are classified as murder under Section 300."),
        ("qa-299/300-6", "What are the exceptions to murder under Section 300 IPC?", "Five exceptions convert murder to culpable homicide not amounting to murder, such as grave and sudden provocation and private defence."),
        ("qa-299/300-7", "What is the maximum punishment for culpable homicide not amounting to murder?", "Imprisonment for life, or imprisonment up to 10 years, and fine."),
        ("qa-299/300-8", "Is culpable homicide under Section 299/300 IPC compoundable?", "No, it is not compoundable."),
        ("qa-299/300-9", "Can a minor be prosecuted for culpable homicide?", "Yes, but if accused is under 18 years, the case is dealt with under the Juvenile Justice Act."),
        ("qa-299/300-10", "Which court tries culpable homicide cases?", "Sessions Court generally tries culpable homicide cases due to their seriousness."),
        ("qa-299/300-11", "Are medical reports necessary in culpable homicide cases?", "Yes, medical reports and post-mortem help to establish cause of death and nature of injuries."),
        ("qa-299/300-12", "Does intention matter in culpable homicide not amounting to murder?", "Yes, both intention to cause death and knowledge that death is likely are considered by courts."),
        ("qa-299/300-13", "What is the role of grave and sudden provocation in culpable homicide?", "It acts as an exception to murder, lowering liability to culpable homicide not amounting to murder."),
        ("qa-299/300-14", "Can abetment of culpable homicide be punished?", "Yes, abetment is punishable under Section 109/120B IPC read with Section 299/304."),
        ("qa-299/300-15", "Are police empowered to arrest without warrant in culpable homicide cases?", "Yes, as culpable homicide is cognizable."),
        ("qa-299/300-16", "What common defences are used in culpable homicide trials?", "Defences include lack of intention, private defence, accidental death, grave and sudden provocation, or insanity."),
        ("qa-299/300-17", "Is there any limitation period for prosecution of culpable homicide?", "No, there is no limitation period; prosecution can proceed at any time."),
        ("qa-299/300-18", "Does conviction for culpable homicide affect government employment?", "Yes, conviction usually bars an individual from government service."),
        ("qa-299/300-19", "Can a conviction for culpable homicide be appealed?", "Yes, the convicted person may appeal in High Court and Supreme Court."),
        ("qa-299/300-20", "What are recent trends in culpable homicide judgments?", "Recent judgments focus on evidence, medical proof, motive, and application of exceptions to distinguish murder from culpable homicide."),
    ]
    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 299/300 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))
    return triplets
