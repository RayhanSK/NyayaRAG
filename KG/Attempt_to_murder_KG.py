def get_attempt_to_murder_triplets():
    triplets = [
        
        ("Section 307 IPC", "criminalizes", "Attempt to Murder"),
        ("Section 307 IPC", "has_ingredients", "Intention or knowledge likely to cause death, plus overt act"),
        ("Section 307 IPC", "maximum_punishment", "up to 10 years imprisonment, or life if hurt caused, plus fine"),
        ("Section 307 IPC", "attempts_by_life_convicts_punishable_by", "death if hurt caused"),
        ("Section 307 IPC", "is_cognizable_offence", True),
        ("Section 307 IPC", "is_bailable_offence", False),
        ("Section 307 IPC", "is_triable_by", "Court of Session"),
        ("Section 300 IPC", "defines", "Murder"),
        ("Section 302 IPC", "prescribes_punishment_for", "Murder"),
        ("Section 308 IPC", "criminalizes", "Attempt to Commit Culpable Homicide"),
        ("Section 308 IPC", "threshold", "Lower than 307"),
       
        ("Section 307 IPC", "proven_by_evidence_type", "Medical Reports & Expert Testimony"),
        ("Section 307 IPC", "proven_by_evidence_type", "Corroboration of Witness Testimony"),
        ("Section 307 IPC", "proven_by_evidence_type", "Confessions (if admissible)"),
       
        ("Attempt to Murder", "requires", "Intention or Knowledge"),
        ("Attempt to Murder", "requires", "Proximate step toward death"),
        ("Attempt to Murder", "act_must_resemble", "Completed murder if successful"),
        ("Section 307 IPC", "distinguished_from", "Section 308 IPC"),
        
        ("Section 307 IPC", "actus_reus", "Overt act toward causing death"),
        ("Section 307 IPC", "mens_rea", "Intention to cause death or knowledge that act is likely to cause death"),
        
        ("H. J. Dileep v. State of Karnataka", "interpreted_section", "Section 307 IPC"),
        ("H. J. Dileep v. State of Karnataka", "established_rule", "Intention and overt act are sufficient for conviction"),
        ("Jayanth v. The State of Karnataka", "interpreted_section", "Section 307 IPC"),
        ("Jayanth v. The State of Karnataka", "established_rule", "Prosecution must prove intention and corroboration"),
        ("R. Prakash v. State of Karnataka", "interpreted_section", "Section 307 IPC"),
        ("R. Prakash v. State of Karnataka", "established_rule", "Deference to trial court’s conviction unless unsupported by evidence"),
    ]

    qa_chunks = [
        ("qa-307-1", "What is the section for Attempt to Murder in the IPC?", "Attempt to murder is covered by Section 307 of the Indian Penal Code (IPC)."),
        ("qa-307-2", "What are the essential ingredients to convict under Section 307 IPC?", "(i) An act by the accused; (ii) The act done with intention or knowledge likely to cause death; (iii) The act must be a proximate step towards causing death. Corroborative evidence supports intention."),
        ("qa-307-3", "Is causing grievous hurt sufficient for Section 307?", "Not necessarily. Grievous hurt may attract Section 307 if prosecution proves the act was done with intention or knowledge of causing death."),
        ("qa-307-4", "What is the maximum punishment for Attempt to Murder?", "Imprisonment up to 10 years, which may extend to life imprisonment in cases where hurt is caused; a fine may also be imposed."),
        ("qa-307-5", "Can Section 307 be invoked if the accused did not cause any physical injury?", "Yes — conviction can be based on the nature of the act and intention even if death or injury did not occur, provided the act was such that it would have caused death if effective."),
        ("qa-307-6", "What is the difference between Section 307 and Section 308 IPC?", "Section 307 deals with attempt to murder; Section 308 penalizes attempt to commit culpable homicide not amounting to murder. The difference lies in degree of intention and severity of the act/result."),
        ("qa-307-7", "Is Section 307 a compoundable offence?", "Generally, Section 307 IPC is non-compoundable (serious offence). However, courts have sometimes quashed proceedings in certain situations where facts justify compromise—these are exceptional and fact-specific."),
        ("qa-307-8", "What kinds of evidence strengthen a Section 307 prosecution?", "Medical reports, weapon recovery, eyewitness testimony, CCTV/forensic evidence, motive, and confessions (if admissible). Corroboration of testimony is important."),
        ("qa-307-9", "How do courts determine 'intention to kill'?", "Courts infer intention from facts: nature of attack, weapon used, targeted body part, prior threats or motive, and whether the act was likely to cause death if successful."),
        ("qa-307-10", "Are there Karnataka High Court decisions that acquit in 307 cases due to lack of corroboration?", "Yes — recent Karnataka HC judgments have set aside convictions under Section 307 where victim testimony was inconsistent and lacked corroboration."),
        ("qa-307-11", "What is the role of medical evidence in 307 IPC trials?", "Medical evidence documents injuries, their nature and severity, and supports inference about whether the act could have caused death; it is crucial corroborative evidence."),
        ("qa-307-12", "Can an accused be convicted under Section 307 if the victim survives with minor injuries?", "Yes — survival does not preclude a 307 conviction if the prosecution proves intent and the act was such that it could have caused death."),
        ("qa-307-13", "Is Section 307 triable by sessions court?", "Yes — Section 307 offences are generally triable by the Court of Session due to seriousness and classification under CrPC."),
        ("qa-307-14", "Does a confession to police help in 307 cases?", "Confession to police is generally inadmissible; only confessions before a magistrate or formal statements are admissible, with caveats. Corroboration is still important."),
        ("qa-307-15", "What is a common defence against a Section 307 charge?", "Defences include lack of intention to kill, lack of corroborative evidence, self-defence, mistake of fact, or that the injuries were accidental or caused in a scuffle without intent."),
        ("qa-307-16", "How many precedents should I include per topic for my dataset?", "For a focused student project, 2–3 landmark precedents plus some recent high-court decisions are recommended; five precedents per topic makes a robust capsule."),
        ("qa-307-17", "Can Section 307 be downgraded to a lesser offence at trial?", "Courts may convict under lesser offences (e.g., grievous hurt) if intention to kill isn't established; the charge may be altered based on evidence."),
        ("qa-307-18", "What is the significance of 'probable consequence' in Section 307?", "The act must be such that if it had caused death, it would amount to murder — courts analyze proximate likelihood of causing death as a consequence of the act."),
        ("qa-307-19", "Should I store statute text or summaries in my RAG dataset?", "Store both: authoritative statute text (for provenance) and a concise plain-language summary (for retrieval and user answers)."),
    ]
    for qa_id, question, answer in qa_chunks:
        triplets.append(("Section 307 IPC", "has_faq", qa_id))
        triplets.append((qa_id, "has_question_text", question))
        triplets.append((qa_id, "has_answer", answer))
    return triplets
