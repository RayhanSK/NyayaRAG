def get_defamation_triplets():
    triplets = [
        # Statute & Structure
        ("Section 499 IPC", "defines", "Defamation"),
        ("Section 499 IPC", "requires", "Imputation intended to harm reputation"),
        ("Section 499 IPC", "is_cognizable_offence", True),
        ("Section 499 IPC", "is_bailable_offence", False),
        ("Section 499 IPC", "is_triable_by", "Court of Session"),
        # Evidence & Doctrine
        ("Section 499 IPC", "proven_by_evidence_type", "Witness Testimony"),
        ("Section 499 IPC", "proven_by_evidence_type", "Medical & Forensic Evidence (if injury alleged)"),
        ("Section 499 IPC", "mens_rea", "Intention to harm reputation"),
        ("Section 499 IPC", "actus_reus", "Making or publishing imputation"),
        # Precedents
        ("Subramanian Swamy v. Union of India", "interpreted_section", "Section 499 IPC"),
        ("Subramanian Swamy v. Union of India", "established_rule", "Right to reputation is part of Article 21"),
        ("Subramanian Swamy v. Union of India", "constitutional_validity", "Section 499 IPC is valid"),
        ("Ram Jethmalani v. Subramanian Swamy", "interpreted_section", "Section 499 IPC"),
        ("Ram Jethmalani v. Subramanian Swamy", "established_rule", "Public figures also protected"),
        ("S. Khushboo v. Kanniammal", "interpreted_section", "Section 499 IPC"),
        ("S. Khushboo v. Kanniammal", "established_rule", "Only specific harm to reputation counts"),
    ]

    qa_chunks = [
        ("qa-499-1", "What is the punishment under Section 499 IPC?", "Punishment includes imprisonment and/or fine as provided by law."),
        ("qa-499-2", "Is Section 499 a bailable offence?", "No, it is generally non-bailable."),
        ("qa-499-3", "Is Section 499 a cognizable offence?", "Yes, police may register FIR and investigate without magistrate approval."),
        ("qa-499-4", "What is defamation according to Section 499 IPC?", "Defamation is making or publishing a false statement about someone, intending to harm their reputation."),
        ("qa-499-5", "Is truth a defence to defamation under Section 499 IPC?", "Truth is a defence if the statement is made for public good."),
        ("qa-499-6", "Can opinions constitute defamation under Section 499 IPC?", "Opinions may be defamatory if they are presented as facts and harm reputation."),
        ("qa-499-7", "What is the maximum punishment for defamation under Section 500 IPC?", "Maximum punishment is two years’ imprisonment, or fine, or both."),
        ("qa-499-8", "Is Section 499 IPC compoundable?", "Yes, defamation is compoundable with court’s permission."),
        ("qa-499-9", "Is defamation under Section 499 IPC triable by Magistrate?", "Yes, usually tried by Magistrate courts."),
        ("qa-499-10", "Can group or companies file a defamation case under Section 499 IPC?", "Yes, companies and groups can file defamation cases if their reputation is harmed."),
        ("qa-499-11", "Is intention required for conviction under Section 499 IPC?", "Yes, intention to harm reputation is an essential element."),
        ("qa-499-12", "Can a juvenile be prosecuted under Section 499 IPC?", "Yes, but proceedings will be under the Juvenile Justice Act."),
        ("qa-499-13", "Can a conviction for defamation under Section 499 IPC be appealed?", "Yes, any conviction can be appealed in higher courts."),
        ("qa-499-14", "Does conviction under Section 499 IPC affect government employment?", "Yes, conviction may affect eligibility for government service."),
        ("qa-499-15", "What are some common defences against defamation charges?", "Truth, fair comment, privilege, and absence of malice are common defences."),
        ("qa-499-16", "Is there any limitation period for filing a defamation case?", "Generally, limitation period is three years from the date of offence."),
        ("qa-499-17", "Is medical evidence required in defamation cases?", "No, medical evidence is usually not needed unless physical harm is also alleged."),
        ("qa-499-18", "Can abetment of defamation be punished under IPC?", "Yes, abetment is punishable under Section 107/108 IPC."),
        ("qa-499-19", "Can apology prevent conviction in defamation cases?", "Tendering an apology may mitigate punishment but does not always prevent conviction."),
        ("qa-499-20", "What are recent trends in defamation cases under IPC?", "Increased focus on online/social media defamation and balancing freedom of speech with reputational rights."),
    ]
    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 499 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))
    return triplets

