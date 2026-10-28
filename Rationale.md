# Rationale for the Romanian PID Rulebook

**Companion to `RO_PID.md`, the Romanian PID Rulebook. Accompanies version 0.3 of that document.**

**Author:** Ministerul Afacerilor Interne, Direcția Generală pentru Evidența Persoanelor<br>
**Version:** 0.3 — 21 Oct 2026<br>
**Feedback:** feedback.pidrulebook@mai.gov.ro<br>
**References:** the bracketed citations used here are those of the Rulebook; Chapter 9 of `RO_PID.md` is the reference list for all of them.<br>
**Status:** **Not normative.** It states why the national decisions in `RO_PID.md` were taken and creates no obligation of its own. `RO_PID.md` governs; where this document and the Rulebook differ, the Rulebook prevails and this document is to be corrected.

---

## What this document is

This document holds the reasoning behind the national decisions taken in `RO_PID.md` — why a
particular value was chosen, why an attribute is issued or declined, and what the alternatives
would have cost. It was separated out so that the Rulebook itself carries the rule and the
minimum needed to verify it, and a reader looking for a requirement is not reading an argument.

Nothing here creates, varies or qualifies an obligation. Where this document and `RO_PID.md`
appear to differ, `RO_PID.md` governs and this document is wrong.

**The Rulebook retains**, and this document does not duplicate: the statement of which ARF or
CIR requirement each provision transposes, which the review obligation in RO_PID_61 depends on;
any note carrying a SHALL, SHOULD or MAY; and the two notes that exist to stop an implementer
making a specific mistake about the encodings.

**Related documents.** `RO_PID_Data_Model.md` states the data model for implementers. The record of
conformance against Topics 3 and 12 in Annex 2 of the ARF is in the Rulebook itself, as its Annexes B
and C; the assessment against the requirements outside those two topics, and the record of what is
still owed and by whom, are held by DGEP separately from the document set.

**Much of the Rulebook is under review**, and a reason given here for a provision so marked is the
reason for the position as drafted, not for a decision that has been taken. **Annex D of `RO_PID.md`
is the register** of what is open; this document does not repeat it, and notes the register number
where a section is affected.

**Sections 5.3 and 5.4 and the whole of Chapter 7 carry no content.** This document keeps their
reasoning. That is deliberate and is not an
oversight: the withdrawn text is retained by DGEP, and the argument for it is the thing most easily
lost between a decision being deferred and the same decision being taken a year later by different
people. A heading below for one of those provisions should be read as *why the
withdrawn text said what it said*, and as an input to settling the Annex D entry rather than as a
justification for anything currently in force.

**This document follows the Rulebook.** There is a heading below for every provision the Rulebook
states and for every identifier it reserves against a withdrawn section, in the order the Rulebook
reads, save RO_PID_49, which was never separately explained. RO_PID_29 and RO_PID_32 are reserved
and unused, and have no entry. There is nothing for an attribute the Romanian PID
does not carry; Chapter 2 of the Rulebook records every attribute it declines, and the reason.

**"This Rulebook" below means `RO_PID.md`.** This document is not a Rulebook and states no
requirement of its own; where the phrase appears in the reasoning it refers to the document that
reasoning explains.

---

## RO_PID_01 — DGEP SHALL be the sole PID Provider of the Romanian PID.

*Why a single PID Provider.* DGEP holds RNEP and generates the CNP, so it is the only body in Romania that can attest the values a Romanian PID carries without reading them from somewhere else — which RO_PID_04 forbids. A second PID Provider would necessarily populate its attestations from a copy of the register, and where the two disagreed no Relying Party would have any means of telling which was authoritative. The prohibition on any other entity using the document type, the namespace or the Verifiable Credential Type is what gives those identifiers their meaning: a Relying Party that recognises `eu.europa.ec.eudi.pid.ro.1` knows, from the identifier alone, which authority stands behind the attributes.

*Why at most one Romanian PID per Wallet Unit.* Two valid logical PIDs held in one Wallet Unit would attest the same person, from the same register, over two administrative validity periods running independently of one another. A correction applied to one would leave the other outstanding and looking correct, and the batch, replenishment and revocation rules would each have to say which of the two they meant. Nothing is gained in exchange: a Wallet Unit already holds many technical PIDs of one logical PID, and that is what makes repeated presentations unlinkable.

*Why the rule binds the Wallet Unit and not DGEP.* The rule is stated in terms the Wallet Unit observes: whether it holds a Romanian PID, which the document type and the `vct` of the technical PIDs it holds tell it, and whether it is requesting a new logical PID under Section 5.1 or a further batch of the one it holds. DGEP is not in that position. It is not told when a User deletes a Romanian PID (RO_PID_46), so a logical PID it has issued, and not revoked, may no longer be held anywhere, and a duty on DGEP to refuse a second logical PID would refuse the User who has deleted the first and enrols again. Bound on the Wallet Unit, the rule leaves that User a path — delete, then enrol — and a Wallet Unit never holds two.

*Why the converse is left open, and said to be left open.* Whether a User may hold a Romanian PID on each of two Wallet Units — the case of a personal and a work device — is a question about the User rather than about the Wallet Unit, and this provision does not answer it. It turns on how identity proofing and revocation reach a second device, which belongs with the enrolment and lifecycle provisions. The Rulebook records the gap expressly rather than leave a reader to infer a prohibition from a rule that does not state one.

## RO_PID_02 — The Romanian PID SHALL be issued at level of assurance high, as defined in the European Digital…

*Why the level is stated in the Rulebook at all.* It follows from the European Digital Identity Regulation, which requires a Wallet Unit to be provided under an electronic identification scheme notified at level of assurance high; the PID is what carries the identity into that Wallet Unit, and a PID issued at a lower level would be the weakest link in a chain the Regulation requires to be strong throughout. Stating it here is nonetheless what makes RO_PID_31 legible. The enrolment process in that provision — the verification of the User's CEI by the eID Server of the MoIA — is there to meet what [CIR 2015/1502] asks for at this level, and a reader who did not know the level would have no way of telling which parts of it are negotiable.

## RO_PID_03 — DGEP SHALL issue every logical Romanian PID in both the format specified in [ISO/IEC 18013-5] and the…

*Neither encoding is optional and neither is a fallback for the other. Chapters 3 and 4 specify both because a Wallet Unit holds both: the [ISO/IEC 18013-5] encoding serves proximity presentation and the [SD-JWT VC] encoding serves remote presentation, and a User who held only one could not transact in the other setting.*

*Why a batch is of one format.* A single Credential Request under [OpenID4VCI] names one credential configuration, and the Credentials it yields share one Credential Format. A batch holding technical PIDs in both formats cannot be requested, so the provision requires a batch in each format under the same authorization instead: the Wallet Unit makes one Credential Request per format with the same Access Token, and the two batches arrive together.

## RO_PID_04 — RNEP SHALL be the authoritative source for every PID attribute derived from civil-status or population…

*Why RNEP and not the CEI.* Both were candidates. The CEI carries a copy of some of the same values, itself derived from RNEP, and a scheme with no central register has no choice but to read from the card — which is why some Member States do. Romania has a central register, so the choice was real, and it matters because the two are known to **diverge in encoding**: a PID populated from the card would not always carry the same bytes as a PID populated from the register, and neither party to a mismatch would be able to say which was wrong. Reading from RNEP removes the question. The CEI is retained for what it is good at — establishing at enrolment who the person enrolling is — and is not a source of attribute values.

*Why no attribute is populated from data asserted by the User.* A PID that attests what its subject told the issuer attests nothing. The rule is stated expressly because the issuance flow passes through the User's device, and an implementer reading only the protocol could reasonably conclude that a value arriving from the Wallet Unit is a value DGEP may sign.

## RO_PID_05 — A string value in a Romanian PID that is taken from RNEP SHALL be carried exactly as recorded there…

*Why the position is stated at all.* Chapter 3 and Chapter 4 already require UTF-8 and forbid transliteration, but they say it as an encoding rule, in the chapter a Relying Party is least likely to read. The party that needs to know is the one comparing a name against its own records, and the failure it is exposed to is silent: a comparison that returns no match is indistinguishable, to the code performing it, from a User who is not the person on file.

*What RNEP actually holds, and why the provision follows it exactly.* RNEP records **the family name and the given names** in upper case, with hyphens and with Romanian diacritics; DGEP have confirmed that the case rule reaches those two values and no others. Two courses are open: carry the value as held, or title-case it for presentation. Carrying it as held is the only one available to an attestation. Case is not presentation metadata here — it is what the register says the name is — and a PID Provider that re-cased a name would be attesting a string no Romanian record contains, with no way for a Relying Party to tell the transformation had happened.

*What is not folded, and why it matters more than the case.* Some national schemes store string values over a single-byte character set, following the conventions of machine-readable travel documents. That makes matching trivial at the cost of discarding information: `IONEȘTEANU` and `IONESTEANU` are different names, and a scheme that stores only the second cannot recover the first. RNEP holds the diacritics, so the PID carries them.

*On the machine-readable zone.* This is the contrast implementers actually hit. The same person's card carries `IONESTEANU` in its machine-readable zone, because [ICAO 9303] admits only `A` to `Z`, `0` to `9` and `<`. Both values are upper case; **they differ only in the diacritics**. A Relying Party that has previously enrolled a User by scanning the card and now receives a PID holds two strings for one name that differ in one character, and neither is wrong. A byte-for-byte comparison fails on it just as completely as if they differed in ten.

*Why some values are carved out.* Four provisions fix a value or its form themselves, and none of the five values they fix is carried as recorded: RO_PID_08 fixes `nationality`, RO_PID_12 fixes `issuing_authority` and `issuing_country`, RO_PID_17 fixes `attestation_legal_category`, and RO_PID_07 composes `birth_place`. Two of them are worth the space here. RO_PID_12 fixes `issuing_authority` as a mixed-case Romanian string: it is not an RNEP value and nothing about the register governs it, and without the carve-out a literal reading of this provision would upper-case the name of the authority. RO_PID_07 composes `birth_place` on a template of its own, expanding the county to its full name and assembling the remainder, so what is carried is a value this Rulebook constructs rather than one it copies.

## RO_PID_06 — `birth_date` SHALL be taken from the date of birth of record in RNEP.

*The first seven digits of the CNP encode a date of birth, but that date is the one recorded at the time the CNP was assigned. Where a subsequent civil-status rectification has changed the date of birth, RNEP is corrected and the CNP is not. Deriving the attribute from the CNP would therefore attest a date the issuer knows to be superseded.*

## RO_PID_07 — `birth_place` SHALL be taken from RNEP.

*Why the county sits in `region` and not inside `locality`.* The choice looks like formatting and is not. [PID Rulebook] defines `region` as *"the name of a state, province, district, or local area"* — a **name**, which is why the full county name is the conformant reading and the two-letter code would have been the departure. It also decides what a User can disclose: RO_PID_26 makes each member of the structure individually disclosable in a [SD-JWT VC] presentation, so a county carried in its own member can be released without the locality, and a county composed into one string with the locality cannot. A Relying Party that needs to know a User was born in a particular county — and there are such Relying Parties, in the administration of records that are organised by county — can be answered without learning the village.

*Why the remainder is one string rather than two members.* The structure has three members and the Romanian rendering has more levels than that: county, territorial administrative unit, and beneath it the *localitate* or *sat*. There is no fourth member to put the last one in, and this Rulebook has no competence to add one — `place_of_birth` belongs to `eu.europa.ec.eudi.pid.1`. Composing the UAT and what sits beneath it into `locality`, with the UAT in parentheses where the two differ, keeps the whole of the recorded place of birth in the attestation at the cost of one indivisible field. The alternative — dropping the *sat* — would attest a place of birth that is not the User's.

*Why the value is not upper-cased.* It is composed by this provision rather than copied from RNEP, and the county name in particular is expanded from a code by DGEP. RO_PID_05 governs values carried as recorded; this one is not.

*Why the country code is derived rather than copied.* RNEP does not hold the country of birth as an [ISO 3166-1] alpha-2 code, and [CIR 2024/2977] requires one. DGEP therefore maps the country of record onto the code set. That is not a second source of truth and does not touch RO_PID_04: the value attested is the country RNEP records, expressed in the code set the Regulation prescribes, in the same way that the county is expressed as a name rather than as the code the register holds.

*What happens when there is no county.* The template assumes a Romanian place of birth, which always has one. A place of birth outside Romania generally does not, and the structure has to remain well-formed. The rule adopted is that `region` is simply omitted and everything below the country goes into `locality`. The alternative — putting a foreign first-level subdivision into `region` — was declined: it would assert an equivalence between a Romanian *județ* and whatever the other State calls its subdivisions that DGEP cannot verify, and a Relying Party filtering on `region` would then be filtering on two different things. `country` is present in every case, so the CDDL requirement that at least one member be present is met without a special rule.

## RO_PID_08 — The `nationality` attribute of a Romanian PID SHALL contain exactly one country code, and that code…

*RNEP records Romanian citizenship — *cetățenie* in the official Romanian text of [CIR 2024/2977]. It is not an authoritative source for a nationality conferred by another State, and DGEP cannot attest to what it cannot verify. This Rulebook therefore defines no domestic attribute for further nationalities. A User holding another nationality evidences it by other means. This choice also avoids the selective-disclosure limitation described in Section 3.1.3: because the array holds a single element, a User disclosing `nationality` in an [ISO/IEC 18013-5]-compliant presentation discloses nothing beyond Romanian citizenship.*

## RO_PID_09 — `email_address` and `mobile_phone_number` SHALL NOT be included in the Romanian PID.

*Neither is person identification data. RNEP is not an authoritative source for either, so DGEP would be attesting to data it cannot verify. Both change far more frequently than the administrative validity period of a logical PID, and a signed attestation of a superseded address or number is worse than no attestation at all: it carries the issuer's authority behind a value the issuer has no means of keeping current. Users who need to evidence contact details to a Relying Party do so by other means.*

## RO_PID_10 — `personal_administrative_number` SHALL NOT be included in the Romanian PID.

*Romania operates no personal identifier distinct from the CNP and does not introduce one for the purposes of the PID. There is therefore no value for this attribute to carry that the CNP does not already carry, and issuing the CNP a second time under a generic administrative name would defeat the purpose of RO_PID_19, which names the attribute for what it is so that a Relying Party requesting it does so knowingly. The `personal_administrative_number` of [CIR 2024/2977] is optional, and declining it is a choice reserved to the Member State; the corresponding entry in the electronic identification scheme is the description of the CNP policy, not of a policy for this attribute.*

## RO_PID_11 — The address attributes, `family_name_birth`, `given_name_birth` and `sex` SHALL NOT be included.

*Every attribute in this table is optional under [CIR 2024/2977], and whether to issue an optional attribute is a choice reserved to the Member State. The choice made here is to issue none of them, so that the Romanian PID attests identity and nothing further. An attribute that a Relying Party does not receive is one it cannot demand, cannot retain, and cannot lose; the mandatory set is what the Regulation requires a PID to prove, and the case for adding to it has to be made attribute by attribute rather than assumed.*

*On the address in particular.* The address of a natural person is the attribute in this table with the widest lawful demand and the shortest useful life. It changes without any change in the identity the PID attests, it would go stale within the administrative validity period of a logical PID, and a Relying Party that needs a current address is better served by an attestation issued for that purpose and re-issued on its own cycle. Declining it also spares this Rulebook the apparatus that carrying an address faithfully would need — the distinction between *domiciliu* and *reședință*, a second address group, and an attribute saying which of the two is being presented — none of which a Relying Party outside Romania could be expected to interpret correctly in any event.

*On `sex`.* [CIR 2024/2977] defines a nine-value range for this attribute of which RNEP holds two. Issuing an attribute whose value range the register cannot populate invites a Relying Party to read significance into which of the nine values it received. Nothing in the identity the Romanian PID attests requires it.

*On the birth names.* `family_name_birth` supports one narrow purpose — establishing continuity of identity across a change of surname — and a Relying Party with a lawful need for it can establish it from civil-status records. It is not needed in order to identify the holder, which is what the PID is for.

## RO_PID_12 — `issuing_authority` SHALL contain the exact string `Direcția Generală pentru Evidența Persoanelor`…

*Why the value is monolingual.* `issuing_authority` is carried in Romanian only and not bilingually. This is the sole home of the reasoning; the Rulebook states only the requirement, together with the operative pointer to where a localised form can be obtained.

`issuing_authority` is single-valued in both encodings — a `tstr` in [ISO/IEC 18013-5], a string in [SD-JWT VC] — so there is no slot for a second language. A composite such as `Direcția Generală pentru Evidența Persoanelor (General Directorate for Persons' Records)` would not be the name of anything: it is neither the legal name of the authority nor a value any register can be matched against.

The attribute identifies a legal entity; it is not display text. The legal name exists in Romanian, and any English rendering is unofficial. Two parties rendering the same authority into English will not reliably produce the same string, which is exactly the ambiguity a fixed normative value exists to prevent.

*The decisive point is that the multilingual slot already exists elsewhere in the stack.* Issuer and credential metadata are explicitly multilingual by design, whereas the attribute is a single string. Putting a second language in the attribute would be duplicating — badly, in one flat string — what the surrounding metadata does properly, one object per language. Three mechanisms carry the translation, each better suited than the attribute:

- **Credential Issuer Metadata** under [OpenID4VCI], published by DGEP. Its `display` parameter is an array with one object per language, each carrying a `name` and a `locale`. It is the most directly relevant mechanism, because every Wallet Unit that obtains a Romanian PID reads this metadata in the course of issuance. RO_PID_34 requires DGEP to publish it, with display entries in at least Romanian and English.
- **The Trusted List** published under [CIR 2024/2980], which carries the registered name of the PID Provider and supports multilingual name entries. It, not the attestation, is the authoritative record of who DGEP is. That list is the List of Trusted Entities of PID Providers, not a Trusted List; see RO_PID_53.
- **`issuing_country`**, fixed at `RO`, which already gives machine-readable provenance without any party needing to parse the authority name.

## RO_PID_13 — `expiry_date` SHALL be computed from `issuance_date`.

*Why the administrative validity is two years, and why it is computed rather than copied.* The obvious alternative is to take `expiry_date` from the CEI on which the logical PID was founded, on the reasoning that a PID should not outlive the document that proved the identity behind it. It is not used, because the link would carry two costs. It would make the administrative validity of a PID unpredictable — a CEI issued to a child runs four or five years, one issued to an adult ten, one issued over seventy has no expiry at all, so a fallback would have to invent a term anyway. And it would make the PID's lifetime depend on a document the User replaces for reasons of their own, so a routine card renewal would shorten or extend the attestation.

A fixed two-year term avoids both. Every logical PID has the same administrative validity, DGEP can compute it without reading the card, and the User's card renewal cycle and PID renewal cycle are independent of one another.

*Why two years.* The number is a national choice and nothing in the EU instruments constrains it — [PID Rulebook] says in terms that *"It is up to the PID Provider to decide whether the logical PID has an administrative validity period"*, and requirements PID_13 and PID_20 ask only that a policy exist relating these dates to the technical validity period, which RO_PID_14 supplies. Two years is short enough that the attribute values in a PID are re-established against RNEP at a reasonable cadence, and long enough that re-enrolment is not a routine annoyance.

*Why the day before the anniversary.* RO_PID_14 provides that the administrative period runs from 00:00:00 on `issuance_date` to 23:59:59 on `expiry_date`. Setting `expiry_date` to the anniversary itself would make the period two years and one day. Taking the day before makes it exactly two years, which is what was decided.

*Why neither date carries a time.* [CIR 2024/2977] defines both as a date "and if possible time", and the permission is not taken. The administrative validity period is administered in whole days; a time of day would assert a precision DGEP does not have, and it would put a time zone into a value that has to mean the same thing to a verifier anywhere. What a date needs instead is a stated convention for the one case where it must be compared against an instant, and RO_PID_14 supplies it: Romanian local time, converted to UTC. A Relying Party that evaluated the two dates against its own local date could be a day out; the provision says not to. No equivalent question arises for `validFrom`, `validUntil`, `nbf` and `exp`, which carry absolute instants with the [RFC 3339] offset fixed at `Z`.

*What the CEI still does, and what it does not.* The identity proofing behind a Romanian PID is performed against a valid CEI at enrolment, under RO_PID_31. What the CEI does not fix is the attestation's administrative life, which is independent of that document's. Where a CEI is invalidated, cancelled or reported lost, that remains a matter for the revocation grounds in Chapter 7 rather than for the expiry date.

*On the distinction between the two validity periods. The technical validity period is a mandatory element of every technical PID and is much the shorter of the two; RO_PID_38 sets it at no more than two months. It is the batching and single-use rules in RO_PID_39, rather than that period, that limit the ability of malicious Relying Parties to track Users through the repeated presentation of the same attestation. The administrative validity period of the logical PID is measured in years. During it, DGEP provides successive technical PIDs to the Wallet Unit without any action being required of the User. When the administrative validity period ends, the User applies for a new logical PID.*

## RO_PID_14 — The relationship between the administrative dates and the technical validity period of a technical PID…

*Three hazards make this provision necessary rather than formal. A `full-date` has no time element while `validFrom` and `nbf` are UTC instants, so the two cannot be compared without a stated convention — and Section 3.1.2 requires `full-date` for both attributes, which makes the ambiguity live. A User shown an `expiry_date` still in the future must not be left holding no presentable PID, which the fifth clause addresses — the clause whose division of the duty is registered at **N8**. And where local law ties the administrative dates to those of a physical document, the policy must accommodate it. Romania's does not: RO_PID_13 computes `expiry_date` from `issuance_date` over two years and expressly forbids deriving it from the expiry of the CEI.*

## RO_PID_15 — `document_number` SHALL NOT be included in the Romanian PID.

*A document number would be constant for the whole administrative validity of the logical PID — a period of years — and would be presented to every Relying Party that requested it. Technical PIDs are deliberately time-limited and rotated in order to deny Relying Parties a stable value on which to correlate presentations across contexts; a constant document number handed out alongside them defeats that measure. The Romanian PID is a digital attestation and is not a physical document requiring a document number for its own identification, and no Romanian administrative process is defined in terms of a PID document number.*

*The Romanian PID accordingly carries exactly one persistent identifier — the CNP. A Relying Party wanting to correlate presentations has to request that attribute explicitly, under the restrictions Section 5.4 will settle at RO_PID_50, rather than obtain a correlator incidentally from a metadata field it had no particular reason to ask for.*

## RO_PID_16 — `issuing_jurisdiction` SHALL NOT be included in the Romanian PID.

*DGEP is a single authority with national competence. There is no subdivision of Romania that issues person identification data, so there is no jurisdiction code to state. Setting the attribute to the county in which the User happened to enrol would be incorrect — that county did not issue the PID — and would disclose the User's place of enrolment to every Relying Party that requested the attribute.*

## RO_PID_17 — `attestation_legal_category` SHALL contain the exact string `PID`.

*These attributes correspond to the indications required by Annex V points (a) and (h) and Annex VII points (a) and (h) of the European Digital Identity Regulation for qualified and public-body electronic attestations of attributes. [PID Rulebook] makes them optional for PIDs. This Rulebook makes them mandatory for the Romanian PID so that a Relying Party can validate a Romanian PID by exactly the same procedure it applies to a QEAA, without a PID-specific code path.*

*What this provision does and does not do.* It fixes the two values; the table in Section 2.6 is what makes the attributes present in every Romanian PID. The distinction matters because a reader looking for the source of the obligation will not find it here.

*Why the `trust_anchor` URL is unsettled and the attribute is not.* The attribute is required and its value is not yet fixed, which is the third form of marking Section 1.3 provides for. A URL is embedded in every attestation issued and cannot be changed retroactively, so it is settled before first issuance rather than guessed at now. Annex D registers it at N9.

## RO_PID_18 — The domestic attributes of the Romanian PID are exactly those listed in the table below.

*Why the set is closed, and closed by amendment.* Requirement PID_06 permits a PID Provider to carry domestic attributes and does not limit how many. The limit is a national one, and it exists because Sections 2.7 and 3.1.5 are the publication PID_07 requires for the domestic namespace, and Sections 2.7 and 4.1.3 the publication PID_16 requires for the domestic type: a domestic attribute issued but not published there would put DGEP out of conformance with the very requirement that authorises domestic attributes. Requiring an amendment makes that impossible by construction — the attribute cannot be issued until the document that publishes it says so.

*Why the cost of adding one is worth paying.* An amendment means a new version of this Rulebook and a revised publication of the scheme of the domestic namespace and type under RO_PID_30. That cost is the point. A domestic attribute is one no Relying Party outside Romania can be expected to interpret, and a domestic set that grew by increments would end in a Romanian PID that only Romanian Relying Parties could read — which is the outcome the EU-wide attribute set exists to prevent.

*Why these two.* The CNP, because Romania operates no identifier distinct from it and a PID carrying no persistent identifier could not support the processes that need one; the age assertions, because they are the minimising alternative to disclosing `birth_date`, and because age attributes left [PID Rulebook] at its version 1.1 and are therefore available only domestically. RO_PID_19 and RO_PID_20 carry the reasoning for each.

## RO_PID_19 — `personal_numeric_code` SHALL contain the CNP of record in RNEP: exactly thirteen decimal digits…

*Why the CNP is a domestic attribute, and the only identifier.* Romania operates no personal identifier distinct from the CNP and does not introduce one for the purposes of the PID. The CNP is carried as a domestic attribute, under its own name, so that a Relying Party requesting it does so knowingly. It is the only unique, persistent identifier a Romanian PID carries: a Relying Party that needs to identify a User across presentations has no alternative attribute available to it, and one that does not need to should request no identifier at all.

*The legal basis.* The CNP is established by Article 6 of [OUG 97/2005], which at paragraph (2) defines it as a *significant number that uniquely individualises a natural person* and at paragraph (3) provides that it is generated by DGEP. Article 6(1) of that instrument, with Article 22(1) of [Law 119/1996] on civil status documents, provides that it is assigned from birth. The Rulebook cites the instruments rather than restating the definition, because the definition is the legislature's and may be amended without reference to this document.

*Why the first digit is constrained, and to 1 to 6.* The first digit encodes the sex and the century of birth, and its range depends on who assigns the CNP. RNEP assigns 1 to 6 to Romanian citizens, which is the population this Rulebook governs; 7 and 8 are assigned to foreign nationals, whom this version does not reach. The range is stated on that basis and not inferred, because a PID Provider validating the digit on a guess would reject a lawfully assigned CNP. **If the scope of the Rulebook ever extends beyond Romanian citizens, this is one of the provisions that moves with it.**

*A CNP is not immutable.* It is reassigned in exceptional circumstances — a material error in the civil-status record, a legal rectification of the date of birth, an official change of gender. The Rulebook does not describe the CNP as permanent for that reason. A change is handled as any other change of value under RO_PID_43: the existing logical PID keeps the value it was issued with, and the User enrols again for a PID carrying the new one.

*What disclosing the CNP entails.* The thirteen digits are structured `S AA LL ZZ JJ NNN C`: a sex-and-century digit, the year, month and day of birth, the county of registration, a sequence number, and a check digit. The CNP is therefore a *speaking* identifier. A Relying Party that obtains it obtains the User's sex, full date of birth, and county of registration as well — three attributes it may not have requested, in circumstances where the presentation interface would show only that a single number was being shared. Naming the attribute for what it is, rather than as a generic administrative reference, is what allows a Relying Party — and particularly one established in another Member State — to recognise what it is asking for. That name is what makes the disclosure visible to the party consenting to it; the recommendation under RO_PID_19 that a Wallet Unit make the consequence of disclosure evident reinforces it, and the request restriction to be settled at RO_PID_50 will.

## RO_PID_20 — `age_equal_or_over` SHALL assert, for each of the age thresholds 14, 16, 18 and 65, whether the User…

*Why the PID carries age assertions when it already carries a date of birth.* A Relying Party that needs to know whether a User is old enough for something needs one bit, and `birth_date` gives it that bit only by also giving the User's exact age, birthday and star sign, none of which the Relying Party asked for or may lawfully retain. An age assertion is the minimising alternative: a Relying Party requesting `age_equal_or_over.18` learns whether the User is an adult and learns nothing else. The thresholds are carried as separate assertions rather than as a single age so that this holds for each of them independently.

*Why all four are always present.* If DGEP issued only the assertions that happened to be true, the set of assertions present would itself disclose the User's approximate age to anyone who received any one of them. Issuing all four, true or false, means the presence of an assertion carries no information and only its disclosed value does.

*Why these four.* Each of the four has an identified use, and no other threshold does. A threshold that no Relying Party requests is not free: it is an additional attribute in every attestation, an additional digest in every Mobile Security Object, and an additional date on which the technical validity period must be truncated under RO_PID_38.

*Age assertions in the PID are attributes of the PID.* They are defined under PID_06 as domestic attributes, age attributes having left [PID Rulebook] at its version 1.1. Romania does not operate a separate electronic attestation of age.

## Chapter 3 — why the [ISO/IEC 18013-5] encoding is mandatory, and not merely offered

Requirement ARB_02 in Topic 12 in Annex 2 of the ARF obliges the author of an Attestation Rulebook to analyse whether a User must be able to present the attestation while in proximity to the Relying Party and without using the internet, and, if so, to require the [ISO/IEC 18013-5] format. **The analysis itself is in the Rulebook, at the opening of Chapter 3**, which is where ARB_02 requires it and where Annex C claims conformance for it; what follows here is why it came out as it did. A Romanian PID is the electronic counterpart of the CEI, and the transactions in which a CEI is presented today are overwhelmingly face-to-face: identification at the counter of a public authority, at a bank, at a notary, in a hospital, and in the course of a police check. In many of those settings the User has no connectivity, the Relying Party has none, or neither does. A Romanian PID that could be presented only over the internet would not serve the purpose for which it is issued. Both encodings are accordingly mandatory under RO_PID_03, and this one is what makes proximity presentation possible.

## RO_PID_21 — An [ISO/IEC 18013-5]-compliant Romanian PID SHALL use the document type `eu.europa.ec.eudi.pid.1`, as…

*The identifier of the domestic namespace is not freely chosen. PID_06 requires it to be generated by appending the [ISO 3166-1] alpha-2 country code, separated by a period, to the namespace identifier of PID_05 with the version number excluded, optionally followed by a version number. For Romania that yields `eu.europa.ec.eudi.pid` + `.ro` + `.1`. A reverse-domain identifier under a national domain would satisfy the uniqueness requirement of ARB_06a in Topic 12 but would still breach PID_06, because PID_06 constrains the construction and not merely the uniqueness of the result.*

## RO_PID_22 — Every domestic attribute SHALL be carried in the `eu.europa.ec.eudi.pid.ro.1` namespace.

*Note on `expiry_date` and `issuance_date`.* [PID Rulebook] permits either `tdate` or `full-date` for these two attributes. This Rulebook requires `full-date`. The administrative validity period of a logical PID is administered in whole days; encoding a time of day would imply a precision that does not exist and would introduce a needless timezone-handling difference between the two encodings of this Rulebook, since Section 4.1.2 encodes both as a date.

## RO_PID_23 — In an [ISO/IEC 18013-5]-compliant Romanian PID, the age assertions SHALL be encoded as the separate…

*Why the two encodings carry the age assertions differently.* In this encoding each threshold is its own top-level attribute of the domestic namespace, and [ISO/IEC 18013-5] makes every attribute individually disclosable. In [SD-JWT VC] the four are members of one `age_equal_or_over` object, and RO_PID_26 makes every nested property individually disclosable. A User presenting a Romanian PID can therefore disclose that they are over 18 without disclosing whether they are over 16, in **either** encoding. Had the two been carried as one structure in the mdoc encoding, that would not have been possible, because [ISO/IEC 18013-5] presents a structured attribute whole — which is the limitation Sections 3.1.3 and 3.1.4 record for `nationality` and `place_of_birth`. The choice is deliberate: an age assertion whose disclosure drags another age assertion with it defeats the purpose of carrying age assertions at all.

*The difference is one of structure only, and implementers should not attempt to reconcile it.* Each encoding uses the shape that gives individual disclosure in that encoding, and the two shapes differ because the two formats differ.

*Why the [SD-JWT VC] side keeps the nested object.* The alternative was four flat claims named for the mdoc attribute identifiers, which would have made the two encodings look alike. It was declined. The object is the form the EU instruments use for this claim, and looking alike is a false economy here: the two encodings are genuinely different in what they allow, and a shape that hides the difference invites an implementer to assume the rest of the difference is not there either. Both forms satisfy RO_PID_26, so nothing turned on disclosability. RO_PID_27 now fixes the object form and the question is closed.

## RO_PID_24 — The `portrait` attribute of a Romanian PID SHALL contain the facial image of record in RNEP — the image…

*Why this provision does not restate the quality requirements.* It did, at length, and the restatement is withdrawn. Two instruments settle the point. [PID Rulebook] provides that mandatory inclusion of `portrait` applies only *"as of 24 months after entry into force of the Regulation amending [CIR 2024/2977]"*, so the attribute is not yet required to carry an image at all. And **ARB_06a** places the duty to fully define the identifier, the syntax and the semantics of an attribute on the Rulebook that owns the **namespace** it sits in. `portrait` sits in `eu.europa.ec.eudi.pid.1`, which is not Romania's namespace; the quality requirements bind DGEP through [CIR 2024/2977] whether or not this Rulebook repeats them, and repeating them creates a second copy that can drift from the first.

*Why no byte figures are carried.* **A number in a normative document is a number somebody has to honour.** A constraint on the encoded size of a portrait is an operational parameter, settled against the population of images it will be applied to and adjusted as that population changes; a figure fixed in a Rulebook can be corrected only by amending the Rulebook. Any such constraint therefore belongs in a technical profile, and RO_PID_24 is where it will be recorded when it is fixed.

*The national requirements for the attribute are registered at **N6** and are to be added to this provision before the value is populated.*

*Why everything portrait is nonetheless gathered here.* The alternative to restating the requirements is scattering what remains — a source rule in one place, an empty-value rule in another, production parameters in a third — and a party implementing the portrait then has to find them. This provision is declared the single home for the attribute, so that when DGEP settles the production parameters, the size constraint and the date from which the value is populated, there is one place for them to go and one place to read.

*What operates in the meantime.* The attribute is present in every Romanian PID and empty. The encoding of an empty portrait is prescribed by PID_03 and stated at RO_PID_25, and a Wallet Unit must make the presence and the emptiness evident to the User, so that a User is not later surprised to learn their PID has always had a portrait slot in it.

## RO_PID_25 — DGEP SHALL enable every User to opt out from receiving a `portrait` attribute.

*The encoding of an empty portrait is prescribed by PID_03 in Topic 3 in Annex 2 of the ARF and is not a national choice. Stating it explicitly matters because "empty" admits of at least four implementations — a zero-length `bstr`, an empty string, an empty data URL, and an absent attribute — which would not interoperate. Note also that the Annex to [CIR 2024/2977] leaves the opt-out to the Member State, which may provide for it, and requires the value to be empty where the User exercises it. This provision is Romania's exercise of that option, and offers it to every User.*

*Whether a User can change their mind, and how.* They can, by deleting the Romanian PID and enrolling again, and making the new election at that enrolment. A technical PID is signed and cannot be edited, so a changed election could otherwise reach the Wallet Unit only on technical PIDs issued later under the same logical PID — and those are issued by replenishment alone, with the values the logical PID was issued with (RO_PID_43, RO_PID_45). A change of election is therefore handled as a change recorded in RNEP is: a new logical PID, with the old one deleted and lapsing unrevoked.

*What that avoids.* Applying a changed election under the existing logical PID would supersede every technical PID already issued: the Wallet Unit would have to stop presenting them (ISSU_62) and DGEP would have to revoke each one still valid for 24 hours or more (VCR_09) — a status-list write per outstanding technical PID, for the one attribute value a User can change at will. A new logical PID supersedes nothing and revokes nothing, and the Rulebook keeps a single rule for every change of value.

*What it costs.* The User goes through the enrolment of RO_PID_31 again to change a display preference, and the two-year term of RO_PID_13 restarts. While the transitional rule in RO_PID_24 applies the cost does not arise in practice: `portrait` is empty whichever election is in force, so a change of election changes no value.

*Why the Rulebook has to say so.* PID_03 places the opt-out "during issuance of a PID" and stops there. It neither provides for a later change nor forbids one, so a Wallet Provider building the setting has nothing to build against. RO_PID_25 says that the election belongs to the logical PID, and how a User who wants another one obtains it.

*On timing.* [CIR 2024/2977] makes the inclusion of `portrait` mandatory as of twenty-four months after the entry into force of the Regulation amending it. This Rulebook requires the **attribute** from the first issuance of a Romanian PID, ahead of that date, and its **value** from the date DGEP announces. The attribute is therefore mandatory throughout, and never optional and never absent; what the transitional rule in RO_PID_24 defers is the image and not the slot.

## RO_PID_26 — In a [SD-JWT VC]-compliant Romanian PID, all claims SHALL be individually selectively disclosable…

*The claims [SD-JWT VC] excepts are those whose function is to establish the validity, type, or key binding of the attestation itself rather than to convey an attribute. They are not enumerated in the Rulebook, so that it does not go stale if that list changes. `iat` is not among them. Section 4.2 of the Annex to [CIR 2024/2977] admits no exception beyond those [SD-JWT VC] defines, so `iat` is selectively disclosable, although it dates the technical PID rather than saying anything about the User.*

## RO_PID_27 — The `age_equal_or_over` claim SHALL be a JSON object whose members are the age thresholds defined in…

*Why the member names are strings and not numbers.* A JSON object key is a string by definition, so `{"14": true}` is the only well-formed rendering and `{14: true}` is not JSON at all. The provision says so because a list of thresholds written `14, 16, 18 and 65` reads as a list of integers, and an implementer working from that list rather than from the example could reasonably produce the second form. The [ISO/IEC 18013-5] encoding gives no help here: there the threshold is part of an attribute identifier, `age_over_14`, and the question does not arise.

*Why a Relying Party may not rely on the ordering.* Nothing in JSON fixes the order of object members, and two conforming serialisers may differ. The point is sharper here than it would be elsewhere, because RO_PID_26 makes each member individually disclosable: a Relying Party frequently receives one member and not the set, so a verifier reading the members positionally would be reading a structure it has not been given. It would also break the first time a threshold was added by amendment.

*Why all four are present whether true or false.* The reasoning is RO_PID_20's — the presence of an assertion must carry no information, or the set of assertions present would itself disclose the User's approximate age. It is restated in this provision because the object form makes omitting a false member the natural implementation, in a way that four separate attributes do not.

## RO_PID_28 — A [SD-JWT VC]-compliant Romanian PID SHALL use the Verifiable Credential Type `urn:eudi:pid:ro:1`.

*Why a domestic type rather than the base type.* `urn:eudi:pid:1` describes the EU-wide PID, which carries neither the CNP nor the age assertions. A Romanian PID presented under the base type would carry claims that type does not declare, and its Type Metadata could not describe them without ceasing to be the metadata of the base type. Requirement PID_14 provides for exactly this case, and this provision takes it.

*Why the type extends rather than replaces.* Extension preserves every mandatory claim of the base type, so a Relying Party that needs nothing domestic can process a Romanian PID against `urn:eudi:pid:1` and never learn that a domestic type exists. A separate, unrelated type would oblige every Relying Party in the Union to learn a Romanian type before it could read a family name, which is the interoperability cost the base type exists to avoid.

*Why the identifier takes this form.* PID_14 requires every PID type to sit in the `urn:eudi:pid:` namespace, and `urn:eudi:pid:ro:1` carries the [ISO 3166-1] alpha-2 country code in the same position, and to the same effect, as the `.ro` in the domestic namespace of RO_PID_21. The two encodings therefore identify Romania in the same way, which is one fewer thing for an implementer building both to remember.

## RO_PID_30 — DGEP SHALL publish the scheme of the domestic namespace `eu.europa.ec.eudi.pid.ro.1` and of the domestic type…

*Sections 4.1 and 4.2 of the Annex to [CIR 2024/2977] require a PID Provider that uses a domestic namespace or a domestic type to publish its scheme in accordance with Article 8 of [CIR 2025/1569], which establishes the catalogue of attestation schemes. That publication is what makes the domestic attributes reachable by a Relying Party in another Member State: without it, such a Relying Party encountering a Romanian PID has no documented means of discovering what the domestic namespace contains. Sections 2.7, 3.1.5 and 4.1.3 of the Rulebook define what the scheme contains.*

## RO_PID_31 — DGEP SHALL issue a logical Romanian PID only after identity proofing and verification meeting the…

*Why enrolment is remote.* A User who holds a CEI already holds a document DGEP itself issued and can verify. Verifying it in the course of a request made from the device the PID is to be issued to lets the whole enrolment happen in one sitting on one device, without an appointment or a journey, and with no gap between the moment the User is identified and the moment the Wallet Unit receives the attestation.

*Why the verification is bound to the Wallet Unit that receives the PID.* An identity established in one place and an attestation delivered to another leave a gap an attacker can stand in. Verifying the CEI within the authorization session the requesting Wallet Unit began, and releasing the authorization code to that session alone, closes it: the device on whose request the User was identified is the device that receives the attestation.

*Why the process names a Wallet Unit, and not RO Wallet.* DGEP issues a Romanian PID to a Wallet Unit of a Wallet Solution it accepts, and Romania publishes the list of those Wallet Solutions so that a prospective User can find it. Every Wallet Provider whose Wallet Solution is certified at national level under the Romanian certification scheme for the European Digital Identity Wallet is obliged by RO_PID_35 to support DGEP and to agree with it the rules under which DGEP processes its requests. The process therefore names a Wallet Unit, not a particular application, and RO Wallet follows it on the same terms as any other.

*Why a requirement of Topic 10 is stated in this Section.* ISSU_21 would otherwise sit with the issuance protocol in Section 5.2. It is stated here instead because the verification it requires precedes every issuance: without it, DGEP has no basis for saying that the Wallet Unit is genuine. The trust anchor that verification works from is one DGEP configures for each Wallet Solution it accepts, and not one drawn from a List of Trusted Entities, which is why ISSU_19 is not adopted. Stating the duty here and the manner of verification in RO_PID_33 keeps the two questions apart: what DGEP must establish before issuing is a matter for the enrolment, how it establishes it is a matter for the protocol.

*Why no separate artefact records the User's authorisation.* The verification of the CEI is the authentication of the End-User that the authorization code flow of [OpenID4VCI] performs at the Authorization Endpoint, and the authorization code is the protocol's own instrument for carrying the result of that authentication to the Wallet Unit. It is released only on a successful verification, is short-lived and single-use, and is bound to the session that requested it. A national artefact serving the same purpose would restate the protocol and would have to be secured again from first principles.

*Why activation is not provided for here.* Requirement ISSU_05 requires a Wallet Unit to support a process to activate a newly issued PID, in accordance with Section 2.2.2 of [CIR 2015/1502], and is addressed to the Wallet Unit. Like ISSU_58, it binds Wallet Units directly, and restating it nationally would add nothing and would risk stating it differently. Its identifier, RO_PID_32, is reserved rather than reassigned, so that the identifiers after it are unchanged.

## RO_PID_33 — Issuance of a Romanian PID SHALL use the OpenID for Verifiable Credential Issuance protocol [OpenID4VCI].

*The batch and re-issuance features of [OpenID4VCI] are required in terms because the rest of this Rulebook assumes both and would otherwise never require either. RO_PID_39 obliges DGEP to issue in batches, RO_PID_42 obliges it to replenish them automatically and RO_PID_44 obliges it to publish the batch size in the `batch_credential_issuance` parameter — none of which is possible unless the protocol feature carrying a batch is implemented. The re-issuance features are the ones replenishment under RO_PID_42 uses: the refresh token issued with the logical PID, presented again for every later batch.*

*Terminology.* Annex 1 of the ARF uses **Wallet Unit Attestation (WUA)** as the umbrella term and defines two concrete subtypes: the **Wallet Instance Attestation (WIA)**, which attests the integrity and authenticity of the Wallet Instance, and the **Key Attestation (KA)**, which attests the certification and properties of the Wallet Secure Cryptographic Device and carries the public keys it holds. Requirement ISSU_21 requires both to be verified. A provision requiring only "a valid Wallet Unit Attestation" would leave it open which of the two was meant, and would not reach the device at all.

*On what the verification is performed against.* Topic 9 in Annex 2 of the ARF, and not Topic 10, is where the two attestations are defined and where most of a PID Provider's duties in respect of them are stated. Requirement WUA_25 fixes the verification of the Wallet Instance Attestation to Appendix E of [OpenID4VCI] and WUA_11a fixes the verification of the Key Attestation to Appendix F.4; WUA_36 binds a PID Provider to [Technical Specification 3]. Each of the first two also requires the attestation to be checked for revocation. The Rulebook adopts neither that check nor requirement VCR_12a, on support for the mechanisms by which it would be made. A requirement to "verify" an attestation without stating the procedure is not implementable by an independent party. Rather than name the Appendices, the provision states the verification DGEP performs: the signature under the certificate in `x5c`, that certificate against the trust anchors configured for the Wallet Solution, and the level of resistance the Key Attestation attests.

*Why the verification follows the steps of the protocol.* Each rule attaches the verification to a request in which the attestation is carried. The Wallet Instance Attestation travels with the client authentication, so it is verified in the Pushed Authorization Request, which opens every first issuance, and in every token request that uses a refresh token, which opens every replenishment. A Key Attestation is verified where one is carried: in the DPoP proof that exchanges the authorization code, which ties the key binding the refresh token to the Wallet Secure Cryptographic Device, and in every Credential Request using the `attestation` proof type. Replenishment is automatic and requires nothing of the User, but it is not a lesser event than enrolment: the Wallet Instance Attestation verified on each refresh is what shows that the request still comes from a genuine Wallet Instance.

## RO_PID_34 — DGEP SHALL publish Credential Issuer Metadata in accordance with [OpenID4VCI] at every service supply point…

*This is where the multilingual name of the PID Provider belongs. The `display` array of the Credential Issuer Metadata holds one object per language, so it can carry the authority name in as many languages as are useful, whereas the `issuing_authority` attribute is a single string and can carry only one. RO_PID_12 keeps the attribute in Romanian for that reason; this provision is what makes an English name available to a Wallet Unit or Relying Party that needs one.*

*Why a duty of the Wallet Unit is stated in a provision about DGEP's metadata.* ISSU_24 is addressed to the Wallet Unit, and it is the other half of what the metadata is for. A User is asked, in the enrolment process in Section 5.1, to have their identity card verified by whatever is at the other end of the flow. Nothing about how a flow is started establishes who is at that end, and the validation of DGEP's access certificate is what establishes that it is DGEP.

## RO_PID_35 — Every Wallet Provider whose Wallet Solution is certified at national level under the Romanian certification…

*This transposes requirement ISSU_23a; ISSU_23b, which is addressed to the Wallet Provider alone, is not restated. It is stated for completeness of the Wallet Provider's obligations under this Rulebook, and is addressed to every Wallet Provider whose Wallet Solution is certified under the Romanian scheme rather than to DGCTI alone, since DGEP issues to a Wallet Unit of any Wallet Solution it accepts under RO_PID_31. DGEP is at present the sole PID Provider of the Romanian PID under RO_PID_01.*

## RO_PID_36 — Every technical PID SHALL be cryptographically bound to a key pair whose private key is generated in, and never…

*The second paragraph admits both proof types [OpenID4VCI] defines. With the `jwt` proof type DGEP verifies possession of each key separately; with the `attestation` proof type it relies on the Key Attestation, which attests every key it lists and the device that holds them. Requirements WUA_09a, WUA_12 and WUA_34 in Topic 9 in Annex 2 of the ARF, which would combine the two for every key, are not adopted.*

## RO_PID_37 — The Romanian PID is a device-bound attestation.

*Requirement ARB_34 in Topic 12 in Annex 2 of the ARF obliges an Attestation Rulebook to state whether its attestation is device-bound. The answer here is not in doubt — device binding is called 'mdoc authentication' in [ISO/IEC 18013-5] and 'key binding' in [SD-JWT VC], requirement ISSU_17 makes it mandatory for every PID, and RO_PID_36 already requires it — but ARB_34 asks for the statement and not for the inference.*

*On the second paragraph.* Requirement ARB_28 permits a Rulebook to define a `cryptographically_bound_to` attribute recording that the Attestation Provider requested a cryptographic binding between the new attestation and an existing PID or attestation at issuance. That mechanism exists so that a subordinate attestation can be tied to the PID that identified its subject. The PID is the attestation others are bound **to**; there is nothing above it in that relationship for it to be bound to in turn.

## RO_PID_38 — The technical validity period of a technical PID SHALL NOT exceed two months from the moment of issuance.

*On the age constraint.* `age_equal_or_over` is the only attribute of a Romanian PID whose value changes on a date DGEP can compute exactly and in advance, and it changes for every User who reaches 14, 16, 18 or 65 — the four thresholds RO_PID_20 fixes, and the only four, since it forbids an assertion at any other. Without this constraint, a technical PID issued shortly before such a birthday would continue to assert that the User had **not** attained the threshold for as long as two months after they had, and RO_PID_43 would oblige DGEP to revoke it — turning every threshold birthday in the country into a revocation event. Truncating the technical validity period so that it ends before the birthday means the situation cannot arise: the assertions in a technical PID are true for the whole of its technical validity period, by construction. The cost is that a User approaching a threshold receives shorter-lived technical PIDs for a time, which RO_PID_42 replenishes automatically and the User does not see.

*Why the period is not tied to the Wallet Instance Attestation, the Key Attestation or the logical PID.* Requirement ISSU_12c would end the technical validity period no later than the revocation maintenance periods of the two attestations presented at issuance, and is not adopted: the revocation of a Wallet Instance or of a Wallet Secure Cryptographic Device reaches a technical PID through revocation under Chapter 7, not through its expiry. Nor is the period cut at the end of the administrative validity period. A technical PID issued shortly before that end runs its ordinary course; what ends with the administrative validity period is replenishment, under RO_PID_14.

*Why two months.* The period is a ceiling on how long a technical PID can be presented without its Wallet Unit going back to DGEP. A longer period serves a User who is offline for long stretches and costs revocation exposure, since a technical PID outlives the event that should withdraw it unless the status list catches it; a shorter one does the reverse and multiplies replenishment. Two months is the national decision on that balance. It is a maximum, and the age constraint in the second paragraph shortens it for an individual technical PID where it binds.

*A technical PID valid for two months is not a short-lived attestation within the meaning of requirement VCR_01 in Topic 7 in Annex 2 of the ARF, which sets that threshold at 24 hours or less. The Romanian PID is therefore a revocable attestation, and the revocation machinery Chapter 7 will provide is not a precaution but the sole means by which an incorrect or withdrawn PID is taken out of circulation. Two of its provisions are to carry that weight: RO_PID_58, on the cascade from a revoked logical PID to the technical PIDs derived from it, and RO_PID_59, on how stale a Relying Party's view of revocation status may be.*

## RO_PID_39 — DGEP SHALL issue technical PIDs to a Wallet Unit in batches, of at most the size it publishes under RO_PID_44…

*The two requirements in the first paragraph are not in tension, and requirement ISSU_11a obliges a Wallet Unit to verify the first of them. "Distinct" here means distinct as an attestation — a different key pair, different salts, different attribute digests and a different issuer signature — and not distinct in content. The key pair is the Wallet Unit's to supply, one for each technical PID it requests; DGEP binds each technical PID to the key presented for it, and issues no more than one for each key. Two technical PIDs of the same batch attest exactly the same facts about the same User; what must differ is everything by which a Relying Party could recognise one presentation as involving the same attestation as another. RO_PID_41 states which elements those are.*

*Batching with single use is what denies Relying Parties a correlator. If a Wallet Unit presented one attestation repeatedly, colluding Relying Parties could correlate those presentations by the attestation itself, regardless of which attributes the User disclosed. A fresh attestation with a fresh key for each presentation removes that correlator.*

*This provision bears that burden alone, with RO_PID_41. The technical validity period in RO_PID_38 does not constrain correlation over an interval of two months, so the batch and the single-use rule are the whole of the measure.*

*Why the Rulebook fixes no batch size.* The size of a batch is an operational parameter. DGEP sets it under the policy requirement ISSU_38 requires it to hold and publishes it under RO_PID_44, in the `batch_credential_issuance` parameter where a Wallet Unit reads it; a figure written into this Rulebook could be changed only by amending a notified document.

## RO_PID_40 — Where a Wallet Unit holds no unused technical PID of the Romanian PID it holds and is unable to obtain a new…

*Why there is no fall-back to re-presentation.* Requirement ISSU_47 would have a Wallet Unit that has run out of unused technical PIDs, and cannot obtain more, fall back to Method B and present an already-used technical PID again. The Rulebook does not adopt it. A technical PID presented a second time carries the same signature, the same digests and the same status-list index as the first time, so every Relying Party that receives it can link the presentations to one another, and can go on doing so for the rest of its technical validity period — up to two months under RO_PID_38. That would undo, for exactly the Users who are offline longest, what RO_PID_39 and RO_PID_41 exist to secure.

*What it costs, and why the cost is small.* A User whose Wallet Unit has exhausted its batch and cannot replenish cannot present the PID until it can. RO_PID_42 requires replenishment to be automatic and opportunistic, and the batch size published under RO_PID_44 is set so that a Wallet Unit reaches that state rarely. Requirement ISSU_46, a warning to the User before it does, is not adopted: the Wallet Unit replenishes whenever it can, and a refusal is what the User sees when it could not.

## RO_PID_41 — DGEP SHALL ensure that every element of a technical Romanian PID that is capable of being unique has a…

*Why the third paragraph is not satisfied by the first.* The elements listed in the first paragraph are values DGEP chooses and can therefore make unique. A timestamp is not chosen — it is observed — and the natural implementation, stamping every technical PID in a batch with the instant the batch was assembled, produces a value that is identical across the batch and almost certainly unique to it. That is a batch identifier in all but name. Note the interaction with RO_PID_38 and RO_PID_39: the technical *validity period* must be identical across a batch, so it cannot be made to differ within one; it can only be made common to many. Rounding every instant to the start of a whole day in the local time of Romania does that — every batch DGEP issues on a given day carries the same values, and two technical PIDs carrying them are no more likely to share a batch than any two issued that day. The cost is precision nobody relies on: a technical PID may begin up to a day before it was issued, never before the administrative validity period, and end up to a day early, and `iat` records the day of issuance rather than the instant.

*Why the discard obligation matters to DGEP and not only to the User.* Retaining the per-attestation salts and digests would leave DGEP holding, in one place, the means to link every presentation of every Romanian PID ever made. The PID Provider is the one party in the ecosystem that could construct such a record, and this provision is what puts it beyond reach. The revocation index and the end of the technical validity period are the exception, because revocation under Chapter 7 cannot be carried out without them; neither appears in a presentation in a form that links one technical PID to another.

*This provision transposes requirements ISSU_35, ISSU_35b and ISSU_36 in Topic 10 in Annex 2 of the ARF, and is the operative content of requirement ARB_22 so far as the privacy of the Romanian PID is concerned. It completes what RO_PID_39 begins. Rotating attestations achieves nothing if the attestations carry a value in common: two colluding Relying Parties comparing an identical attribute digest, an identical signature, or an identical revocation index would link the two presentations exactly, without needing any attribute the User disclosed.*

## RO_PID_42 — Replenishment of technical PIDs SHALL be automatic and SHALL NOT require any action by the User, for as long as…

*Why replenishment asks nothing of the User.* A User who has to act to keep a PID presentable will at some point fail to, and will find out at the point of use. Requirement ISSU_42 asks for re-issuance to need no User action to the maximum extent possible, and requirement ISSU_41 that the User not notice the method in use; automatic replenishment is how both are met for the Romanian PID.

*Replenishment and re-issuance.* Topic 10 in Annex 2 of the ARF uses *re-issuance* for every issuance of technical PIDs under an existing logical PID, whether the Wallet Unit asks for them unprompted or the User asks. The Rulebook keeps the two apart. **Replenishment** is what the Wallet Unit does by itself when its supply runs low; **re-issuance** would be what the User asks for, by a re-issue option in the Wallet Unit, and the Rulebook provides for none (RO_PID_45). Where a requirement on re-issuance is transposed — ISSU_42 here, ISSU_63, ISSU_65 and ISSU_60 elsewhere — it is applied to replenishment.

*Why the Wallet Unit sets the lower limit.* The point at which to replenish depends on how the Wallet Unit is used and how often it is online, which the Wallet Unit knows and DGEP does not. Requirement ISSU_45 would have DGEP publish the limit in the `credential_reuse_policy` parameter; this Rulebook does not adopt that parameter (RO_PID_44), and its first sentence, which leaves the Wallet Unit to hold a limit, is what remains.

*Why opportunistically.* The lower limit protects only a Wallet Unit that is online when it is reached. One that replenishes whenever connectivity is available enters a period without connectivity holding as many unused technical PIDs as it can, which is when it needs them.

## RO_PID_43 — The value of every attribute and metadata element in a technical PID SHALL be valid at the timestamp in the…

*Why a change of value is left to a new logical PID, and the existing one is kept until then.* A change to a value the PID carries — a family name on marriage or divorce, a CNP on rectification — is an event in the User's identity record. The Rulebook does not issue the changed value under the existing logical PID: enrolment establishes the User's identity afresh, so the new value is attested on the same footing as the values it replaces. Nor does it revoke the existing logical PID when the change is recorded. DGEP is not informed of the change, so there is no event on which a revocation could turn; and a revocation would in any case leave the User without a Romanian PID until they enrol again. Keeping the existing logical PID replenished means the User always holds a presentable PID, and chooses when to move to the new one.

*What it costs.* A technical PID issued after the change carries a value that is no longer current, and a Relying Party receiving it receives the superseded value. That is a departure from requirements PID_12 and PID_19, which require every value to be valid when the technical PID becomes valid, and from requirement VCR_09, which requires technical PIDs to be revoked when a value changes; the Rulebook records all three. It lasts until the User applies for a new logical PID or the administrative validity period of the existing one ends. Neither the User nor their Wallet Unit is notified of the change, so it is for the User, who knows that their record has changed, to enrol again. The new logical PID starts a new two-year term under RO_PID_13 — one of the two cases, with a change of the portrait election under RO_PID_25, in which the Rulebook leaves it to the User to act, where requirement ISSU_42 asks for no User action in re-issuance to the maximum extent possible.

*Why the User deletes the existing PID first.* A Wallet Unit holds one Romanian PID at a time (RO_PID_01), so a User enrolling for the changed value on the same Wallet Unit deletes the Romanian PID it holds before enrolling again, and the two are never held together. The deletion revokes nothing, as no deletion does (RO_PID_46); the deleted logical PID is held by no Wallet Unit, is no longer replenished, and lapses at the end of its administrative validity period.

*This provision transposes requirements PID_12 and PID_19 in Topic 3 in Annex 2 of the ARF, save for the case of a changed value, in which it departs from them.*

*Operational consequence of the two-month period.* A batch is ordinarily exhausted by presentation rather than by the passage of time. Two consequences follow, and the design of every Wallet Solution has to account for them.

First, **the batch size is the binding constraint on availability.** A User who exhausts a batch has no unused technical PID for the remainder of the period. RO_PID_42 requires replenishment to be automatic, and a Wallet Unit that replenishes opportunistically whenever connectivity is available, rather than waiting until its supply is spent, avoids the failure; but the size of the batch, not the frequency of replenishment, is what determines whether a User runs out. A Wallet Unit retains presentable technical PIDs across long periods without connectivity, so proximity presentation is not constrained by the technical validity period.

Second, **the number of technical PIDs outstanding at any moment is large**, and the status lists Chapter 7 will provide for are correspondingly large.

## RO_PID_44 — The Romanian PID uses Method A — once-only attestations, specified in requirements ISSU_43 to ISSU_47 in Topic…

*Method A is what RO_PID_39 already describes, and naming it here is what tells a Wallet Unit the method. Requirements ISSU_39, ISSU_39a, ISSU_40 and ISSU_40a, and the second sentence of ISSU_45, would also have the method, the batch size and the lower limit published in the `credential_reuse_policy` parameter of [ETSI TS 119 472-3]. That parameter is not adopted: DGEP publishes the batch size in the `batch_credential_issuance` parameter of [OpenID4VCI], which a Wallet Unit already reads, the method is fixed by this Rulebook, and the lower limit is the Wallet Unit's own under RO_PID_42. The batch size is published rather than fixed in this Rulebook because it is an operational parameter that DGEP must be able to adjust without an amendment.*

*Requirement ISSU_38 obliges a PID Provider to fix the technical validity period and the batch size by a documented policy resting on a linkability risk analysis. That policy is DGEP's and sits outside this Rulebook. The Rulebook fixes the maximum technical validity period, which is a national decision, and leaves the batch size to be set under that policy and published.*

## RO_PID_45 — Replenishment under RO_PID_42 is the only means by which technical PIDs are issued to a Wallet Unit…

*This provision transposes requirements ISSU_65 and ISSU_60 in Topic 10 in Annex 2 of the ARF, in that order, applied to replenishment.*

*Why there is no re-issuance at the User's request.* Under RO_PID_43 a logical PID keeps the values it was issued with, so technical PIDs requested by the User under it would carry exactly what replenishment already delivers without being asked. What a User might want from a re-issue option — a changed name, a changed portrait election, a PID that can no longer be replenished — the existing logical PID cannot supply, and enrolment can. A User who wants a fresh PID therefore deletes it and enrols again, and the Rulebook provides for no re-issue option.

*Why a Wallet Unit does not request technical PIDs on finding one revoked.* Nothing in Sections 5.1 and 5.2 revokes a technical PID while its logical PID stays valid: no change of value or of election is applied under an existing logical PID, so no technical PID is ever superseded. A Romanian PID found revoked is therefore not replaced by a request from the Wallet Unit, and a User whose logical PID can no longer be replenished enrols again.

*On the first rule.* ISSU_65 is the limb of this provision addressed to DGEP rather than to the Wallet Unit, and it is the one with a security consequence: without it, a party who obtained the credentials of a replenishment request could have fresh Romanian PIDs delivered to a device that is not the User's. Section 14.5 of [OpenID4VCI] describes the mechanism the ARF contemplates — a device-bound refresh token issued at first issuance and required at every later issuance — and DGEP's implementation of RO_PID_33 has to provide for it. ISSU_65 speaks of re-issuance; the provision applies it to replenishment, which is the form re-issuance takes for a Romanian PID.

## RO_PID_46 — A Wallet Unit SHALL enable the User, at any time, to delete a Romanian PID from it.

*Of the rules of this provision, the first matters more here than it would elsewhere: because RO_PID_39 puts a batch rather than a single attestation into the Wallet Unit, deleting "the PID" is ambiguous unless the Rulebook says which, and a deletion that left unused technical PIDs behind would leave presentable attestations in a Wallet Unit the User believes no longer holds any.*

*The fourth rule is not in Topic 51 and is required by the interaction between two provisions that are.* RO_PID_42 requires replenishment to be automatic, to require no action by the User, and to continue "for as long as the logical PID is valid and not revoked". Deletion satisfies neither of the conditions that stop it: the logical PID remains valid, and it is not revoked. PAD_03 then forbids the Wallet Unit to tell DGEP anything about the deletion, so DGEP cannot stop replenishing on its own initiative and must not be expected to. Without this rule the conforming behaviour would be for the Wallet Unit to delete the PID at the User's request and silently obtain a fresh batch of it, which is the opposite of what the User asked for. The obligation is therefore placed on the Wallet Unit, which is the only party that knows.

*On what deletion is not.* It is a decision by the User about their own device, not a statement about the validity of the PID. DGEP is not told, no status list changes, and the logical PID remains valid for the remainder of its administrative validity period. This is also why deletion appears here and not in Chapter 7.

**The entries below explain provisions that carry no content.** Their identifiers are reserved in
version 0.3 and the text they once explained is held by DGEP. They are kept because the argument for a
deferred design is the thing most easily lost between a decision being put off and the same decision
being taken later by different people. **None of them states a requirement**, and an implementer
building to any figure or rule mentioned in them is building to something the Rulebook does not say.

| Reserved for | Identifiers | Settles with |
|---|---|---|
| Sections 5.3 and 5.4 — presentation, restrictions on requesting | RO_PID_47 to RO_PID_52 | **N12** |
| Chapter 7 — revocation | RO_PID_56 to RO_PID_60 | **N13** |

---

## RO_PID_47 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_47 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns what a Wallet Unit may present.

*These two paragraphs transpose requirements RPA_08 and RPA_07c in Topic 6 in Annex 2 of the ARF. The second is the only point at which the ARF imposes a SHALL on what a Wallet Unit must show a User about a particular PID attribute, and the Romanian PID carries the attribute it concerns. It sits alongside, and is stricter than, the recommendation in RO_PID_19 about the CNP: a portrait is biometric data within the meaning of Union data protection law, and RO_PID_52 governs what the Relying Party may do with it once obtained.*

## RO_PID_48 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_48 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns proximity presentation and the prohibition on server retrieval.

*The first paragraph transposes requirements ProxId_01, ProxId_01a and ProxId_05 in Topic 24 in Annex 2 of the ARF, and the second transposes ProxId_02, which is addressed to PID Providers by name.*

*Why the prohibition matters more to a PID than the requirement does.* Under server retrieval a Relying Party does not obtain attributes from the Wallet Unit at all: it presents a token received from the Wallet Unit to the issuer and obtains the attributes directly from it. For a Romanian PID that would mean DGEP learning the identity of every Relying Party the User transacts with, and the time of every transaction — the issuer-side observation that the whole design of Chapter 5 exists to prevent. RO_PID_41 discards the per-attestation elements by which DGEP could reconstruct a linkage record after the fact; server retrieval would hand DGEP the same picture prospectively and by design. The prohibition is therefore not an interoperability preference but the counterpart in Chapter 5 of what RO_PID_41 does in issuance and RO_PID_57 in revocation.

*The proximity analysis required by ARB_02 is recorded in the opening of Chapter 3. This provision is the mechanism by which the conclusion of that analysis is implemented.*

## RO_PID_50 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_50 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns when the national identification number may be requested.

*What this provision does.* It states the condition on which a Relying Party may request the national identification number. RPRC_21, which warns a User where a request exceeds the attributes a Relying Party registered, operates on the registered attribute set and is not the route by which this provision takes effect; the condition here is one a Relying Party applies to itself, and the general law applies to it independently.

*Why that matters more here than it would elsewhere.* The CNP is the only persistent identifier a Romanian PID carries, so every request for persistent identification lands on it, and it is a *speaking* identifier — a Relying Party that obtains it obtains the User's sex, date of birth and county of registration as well. That is why the provision is drafted as a condition on the request rather than as a preference, and why it works together with the display obligation in RO_PID_47, which is what makes the disclosure visible to the User approving it.

*The CNP is not merely an identifier. Its thirteen digits encode the User's sex, full date of birth, and county of registration. A Relying Party that obtains it obtains those three attributes as well, whether or not it requested them and whether or not it intends to use them.*

## RO_PID_51 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_51 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns requesting an identifier a Relying Party does not need.

*The CNP is a stable, lifetime-unique value, which is what makes it attractive as a database key and what makes it dangerous as one. Two Relying Parties that each hold it can join their records on it exactly, and neither needs the other's cooperation to do so. Since RO_PID_15 leaves the Romanian PID with no other persistent identifier, the ordinary pressure on a Relying Party is to request the CNP for purposes an opaque number would serve. RO_PID_50 and this provision exist to resist that pressure: the absence of a low-disclosure identifier is a reason to request no identifier, not a reason to request the high-disclosure one.*

*Taken together, these allow the pattern that most Relying Parties actually need: verify the User's identity once against the PID, bind a Pseudonym to that verification, and recognise the User by the Pseudonym thereafter — retaining no identifier from the PID at all. A Relying Party that adopts it satisfies RO_PID_50 and RO_PID_51 without giving up anything it needed.*

*This note is informative. Pseudonyms are a function of the Wallet Unit, governed by Topic 11 in Annex 2 of the ARF and by [CIR 2024/2979]; nothing in this Rulebook adds to or varies those requirements.*

*What a Relying Party does in the meantime.* Where a Pseudonym is not available to it, the alternatives RO_PID_51 names are the Relying Party's own — an account, a pseudonymous identifier of its own, or a prior authentication. A Relying Party that has none of those, and a lawful basis for the CNP, is not in breach of RO_PID_50 by requesting it. The provision does not depend on Topic 11 having shipped; the pattern described above becomes available when it does.

*The alternative that RO_PID_51 assumes.* Topic 11 in Annex 2 of the ARF requires every Wallet Unit to enable a User to generate a Pseudonym and register it at a Relying Party (PA_01), and to authenticate with that Pseudonym on subsequent visits to the same Relying Party (PA_02). Two of its properties make a Pseudonym the mechanism a Relying Party should reach for in place of the CNP:

- A Wallet Unit does not reveal the same Pseudonym to different Relying Parties, unless the User explicitly chooses otherwise (PA_16). Absent such a choice, Pseudonyms held by different Relying Parties therefore cannot be joined, whereas the CNP held by each of them can be, exactly and without their cooperation — and without the User's knowledge, let alone their choice.

- Where a Pseudonym is registered in the course of a presentation of a PID to the same Relying Party, that Relying Party can verify that the same User performed both actions (PA_12).

## RO_PID_52 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_52 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns retention of the portrait by a Relying Party.

*This provision transposes requirement PID_03a in Topic 3 in Annex 2 of the ARF. It is the only provision of this Rulebook that governs what a Relying Party does with an attribute after obtaining it, rather than whether it may request it. It is placed here because both questions are settled at the point of a presentation request, and because a Relying Party reading only the restrictions on requesting would otherwise never encounter it.*

## RO_PID_53 — Romania SHALL notify DGEP as a PID Provider to the Commission as specified in the European Digital…

*Rows 3 and 4 of the notification table are the two most easily overlooked.* The trust anchor that authenticates a status list is not the trust anchor that signs a PID, and RO_PID_54 governs only the latter; a status list that a Relying Party cannot authenticate is a status list it cannot act on. Requirements PPNot_03, PPNot_03a and PPNot_04 are what impose the three assurances the provision states.

*Row 4 matters beyond notification.* The private key of that access certificate is what signs the Credential Issuer Metadata under RO_PID_34, so a Wallet Unit that cannot authenticate the certificate will not be able to rely on the metadata either.

*Notification and registration are separate obligations with separate consequences, and are easily conflated. Notification under Topic 31 is what puts DGEP's trust anchors where a Relying Party can find them, and is what the rest of this chapter governs. Registration under Topic 27 is what makes DGEP a recognised PID Provider in the first place, and it may cause a registration certificate to be issued to it under RPRC_13, whose contents RPRC_15 requires to state the attestation types registered here; this Rulebook does not use that certificate in the issuance of a Romanian PID (RO_PID_34). The two duties in the final paragraph of the provision are requirements Reg_10e and Reg_08, which bind a PID Provider directly; the vetting is the Member State's under Reg_19, which requires it to approve a PID Provider against a defined policy before entering it in the registry, and under Reg_20, which requires it to identify PID Providers at a level of confidence proportionate to the risk. Both are outside this Rulebook.*

*On the list a Relying Party actually goes to.* [PID Rulebook] Section 6 says the Commission publishes the trust anchors of notified PID Providers in a **Trusted List**, and [PID Rulebook] prevails over the ARF where the two disagree, which would point a Relying Party at a Trusted List. The disagreement is resolved by fact rather than by drafting: the Commission publishes the list of PID Providers as a **List of Trusted Entities** under [ETSI TS 119 602], which is what PPNot_05 and PPNot_07 in Annex 2 of the ARF require and what the published list is. A Rulebook that directed Relying Parties to a Trusted List would direct them to something that does not hold DGEP's trust anchors, and Romanian PIDs would be unverifiable by any Relying Party that followed it. Chapter 6 therefore follows the ARF on this point and not [PID Rulebook].

## RO_PID_54 — The private keys used by DGEP to sign Romanian PIDs SHALL be generated and held in a hardware security…

*The certification levels above are stated as a minimum. This Rulebook specifies the assurance level required and not a product; replacing a module with any other meeting these levels does not require an amendment to this Rulebook.*

*Why DGEP operates the infrastructure, and why it matters.* The alternative — DGCTI operating the signing service on behalf of DGEP — creates a problem no drafting can solve. DGCTI is the Wallet Provider of RO Wallet, and **WIAM_12a** in Topic 40 in Annex 2 of the ARF forbids a Wallet Provider to learn which attestations a Wallet Instance holds. The signing service of the sole PID Provider sees every issuance and every replenishment, so placing it with the Wallet Provider would route to that Wallet Provider precisely the knowledge WIAM_12a denies it, by a path the requirement does not contemplate and no drafting can close. **DGEP operating its own signing infrastructure removes the position rather than mitigating it**, which is the only clean answer, and it also puts the keys that sign a PID in the hands of the authority accountable for the PID.

## RO_PID_55 — DGEP, RO Wallet and Relying Parties SHALL use only cryptographic algorithms included in the agreed list.

*Why the provision does more than transpose OIA_03 and WUA_04.* Those two requirements constrain the set an algorithm may be drawn from and select nothing from it. That is the right shape for a requirement addressed to the whole ecosystem, and the wrong shape for a national Rulebook whose stated purpose, in Section 1.1, is that a party implementing or verifying a Romanian PID need not consult anything else. A Relying Party in another Member State that receives a Romanian PID has to verify a signature, and it cannot do that from a permitted set; it needs to know which algorithm was used. Two implementations that each conform to a permitted-set constraint and choose differently do not interoperate, and neither has departed from the text. Naming a mandatory-to-implement set is what removes that outcome.

*Who publishes the profile.* The technical profile is DGEP's. A profile fixes what DGEP issues, so it is published in the name of the party bound by it — and since DGEP also operates the signing infrastructure under RO_PID_54, the party that publishes the profile is the party whose keys apply it.

*Why ECDSA with P-256 and SHA-256.* It is the algorithm the surrounding specifications assume: it is COSE algorithm `-7`, the default of the [ISO/IEC 18013-5] and [SD-JWT VC] ecosystems, supported by every Wallet Secure Cryptographic Device the Romanian PID is expected to be issued into, and present in the [ECCG Agreed Cryptographic Mechanisms]. Choosing anything stronger would exclude hardware without adding assurance the rest of the design relies on; choosing anything else would be a departure from what implementers already build.

*Why the set is a floor and not a closed list.* Curve and hash agility is the one property a document of this longevity cannot do without — the Rulebook outlives by many years the two-year administrative validity period of any PID issued under it — and an amendment to this Rulebook is a slower instrument than a published profile. The third paragraph therefore lets DGEP add algorithms without an amendment, subject to two constraints that between them prevent the discretion from undoing the provision: anything added must itself be in the [ECCG Agreed Cryptographic Mechanisms], and nothing required here may be withdrawn while a technical PID using it is still valid. A profile that could remove an algorithm in current use would strand attestations already in circulation.

*The table is a national election and is what makes this Rulebook implementable. A Relying Party in another Member State encountering a Romanian PID has to verify a signature, and a party building against this Rulebook has to choose an algorithm; a constraint that names only a permitted set leaves both of them to guess, and two conforming implementations that guess differently do not interoperate. Naming a mandatory-to-implement set removes that failure without closing the door on others, which is what the third paragraph preserves.*

*The [ECCG Agreed Cryptographic Mechanisms] is maintained outside this Rulebook and is revised. It is one of the instruments RO_PID_61 requires this Rulebook to be reviewed against, and a revision that withdrew any algorithm named above would require this provision to be amended.*

## RO_PID_56 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_56 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns publication of revocation status.

*The two encodings do not share a revocation mechanism, and an implementation that publishes only one is not conformant for the other. VCR_11 governs [ISO/IEC 18013-5]-compliant PIDs and routes them to the CBOR mechanism carried in Annex 2 of [CIR 2024/2979], the text of which is taken from the forthcoming second edition of [ISO/IEC 18013-5]. VCR_11a governs [SD-JWT VC]-compliant PIDs and routes them to [Token Status List]. Because RO_PID_03 requires every logical Romanian PID to be issued in both formats, DGEP operates two status list services and not one.*

*Why an Attestation Status List and not an Attestation Revocation List.* VCR_01 permits either for the [ISO/IEC 18013-5] encoding, and requirement ARB_23 in Topic 12 obliges this Rulebook to state which. An Attestation Revocation List enumerates the identifiers of revoked attestations, which requires each technical PID to carry a distinct identifier that is disclosed on presentation — a correlator of exactly the kind RO_PID_15 and RO_PID_39 exist to deny. An Attestation Status List carries an index into a bitstring instead, which discloses nothing beyond the index itself. VCR_11a also makes an Attestation Status List the only option for the [SD-JWT VC] encoding, so choosing it for both keeps the two encodings aligned.

*The technical validity period in RO_PID_38 does not make revocation unnecessary. VCR_01 and VCR_01b excuse a PID Provider from operating a revocation mechanism only where every attestation it issues is valid for 24 hours or less, which is not the case here.*

## RO_PID_57 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_57 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the operation of the status lists.

*The first is the most consequential.* RO_PID_15 declines to issue `document_number` on the ground that a constant value presented alongside rotating technical PIDs would defeat the rotation. A status-list index is exactly such a value — it is carried in the technical PID, it is disclosed to every Relying Party that receives it, and if indices were assigned sequentially as PIDs were issued then two indices from one batch would be adjacent, and adjacency would identify the User as surely as a document number. Randomising the index is what prevents the revocation mechanism from reintroducing, in Chapter 7, precisely the correlator Chapter 2 refuses to create.

*The second protects the User against DGEP rather than against a Relying Party.* If a list were small enough, DGEP could infer from a request for it which PID had probably just been presented, and to whom. That is a form of issuer-side tracking that the Regulation does not permit and that the User has no means of detecting.

*The third protects against both.* Requiring authentication to download a list would give DGEP a record of which Relying Parties check which lists and when — again, a picture of where Users are transacting, assembled by the party least able to justify holding it.

*These transpose requirements VCR_17, VCR_18 and VCR_16 in Topic 7 in Annex 2 of the ARF, and each of them closes a way in which the revocation mechanism could undo what the rest of this Rulebook does.*

## RO_PID_58 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_58 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the cascade from a revoked logical PID.

*Revoking only the logical PID would leave outstanding technical PIDs valid for up to two months after the ground for revocation arose, which for grounds such as the death of the User or the compromise of a Wallet Unit is the period during which revocation matters most. The technical validity period places no useful bound on that exposure. The cascade is the only mechanism that removes an outstanding technical PID from circulation.*

*The prohibition is requirement VCR_04 in Topic 7 in Annex 2 of the ARF. A revocation that can be reversed is not a revocation: a Relying Party that has cached a status list, as RO_PID_59 and requirement VCR_15 both contemplate, would continue to treat a reinstated PID as revoked until its cache expired, so reversal produces a period in which the same PID is valid for some Relying Parties and revoked for others.*

## RO_PID_59 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_59 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns revocation checking by Relying Parties.

*Republishing on a fixed schedule regardless of change keeps the publication interval from disclosing whether a revocation has occurred, and gives Relying Parties a predictable freshness bound.*

*Why 24 hours here and two months in RO_PID_38.* The two intervals answer different questions and are not to be aligned with one another. This provision bounds how far out of date a Relying Party's view of revocation status may be, and it is the only provision that bounds it. Setting it in step with the technical validity period would mean a revoked Romanian PID could be accepted for up to two months after its revocation.

*On the strengthening of VCR_13, and on the case it does not cover.* Requirement VCR_13 in Topic 7 in Annex 2 of the ARF states revocation checking as a SHOULD, and requires a Relying Party that departs from it to perform a risk analysis first. This provision makes checking a SHALL, which is a deliberate national strengthening of a choice the ARF leaves open, and it is permitted because it forbids nothing the ARF requires.

*It does not follow that revocation information is always available.* Requirement VCR_14 obliges a Relying Party to reach a reasoned decision where it is not, and the paragraph above transposes it. The case is not hypothetical for the Romanian PID: an [ISO/IEC 18013-5]-compliant presentation takes place over a proximity link, and a Relying Party Instance operating without connectivity holds only what it has cached. That is exactly the situation in which a fresh status list cannot be obtained and the cached one may have aged past 24 hours. The final sentence, which reflects requirement VCR_15, is what makes such a cache available in the first place; a Relying Party that fetches a list only when a User presents a PID both fails offline and discloses to DGEP when it is transacting.

## RO_PID_60 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_60 carries no content in version 0.3 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the grounds on which DGEP revokes.

*Why the Wallet Instance and device ground is drafted as a duty and not only as a ground.* Every other ground in the table is an event that reaches DGEP: a death or a change of citizenship is recorded in RNEP, a lost Wallet Unit is reported, a User asks. This one is not. The revocation of a Wallet Instance or of a Wallet Secure Cryptographic Device happens at the Wallet Provider, and nothing carries it to DGEP; the revocation references in the Wallet Instance Attestation and the Key Attestation are the means by which DGEP can find out, and they only work if somebody looks. A ground that nobody is obliged to look for is not a control, which is why WURevocation_18 and WUA_29 are both drafted as a continuing verification duty rather than as a trigger, and why this provision follows them.

*Why 24 hours, when the ARF says only "regularly".* The figure is national and is derived from the rest of Chapter 7 rather than chosen freely. RO_PID_59 already republishes each status list every 24 hours and already requires a Relying Party to work from a list no older than that. Setting the verification interval to the same figure makes the whole path bounded by one number: a device is revoked, DGEP detects it within 24 hours, revokes immediately, the status list carrying that revocation is republished within 24 hours, and the Relying Party is working from a list within its own 24-hour window. A longer verification interval would place the delay at the head of that chain, where none of the later bounds can recover it — the status list cannot publish a revocation DGEP has not yet made. It also lets DGEP run one daily cycle rather than maintain two schedules, and it aligns with the 24-hour threshold that VCR_09 already sets and that RO_PID_43 already uses.

*Why the second limb costs nothing.* RO_PID_33 already requires both attestations to be verified before issuance. Applying that to every batch rather than only to the first is not new work; it is the removal of an unstated assumption that replenishment under RO_PID_42, which is automatic and requires no action by the User, is somehow a lesser event than first issuance. It is not: it puts fresh, presentable attestations into a device that may since have been revoked.

*This transposes requirement WURevocation_11 in Topic 38 in Annex 2 of the ARF, which obliges a Wallet Provider to revoke a Wallet Unit on the explicit request of a PID Provider in that case, and requirement WUA_08 in Topic 9, which is what puts the Wallet Instance identifier in the Wallet Instance Attestation so that the request can be made. Without this paragraph, DGEP would revoke the PID of a deceased User and the Wallet Unit holding it would continue to exist, with whatever else it holds. Note that the Wallet Provider is required by WURevocation_12 to verify that the requesting party is a PID Provider listed in the List of Trusted Entities of PID Providers before acting on such a request; DGEP's ability to make the request therefore depends on its notification under RO_PID_53.*

*This transposes requirement WURevocation_18 in Topic 38 in Annex 2 of the ARF, which requirement WUA_29 in Topic 9 states in the same terms. It is the only ground in the table above that is a continuing obligation on DGEP rather than an event reported to it, which is why it is stated separately: a ground that nobody is required to look for is not a control. The second limb also closes the case of a Wallet Unit whose device has been revoked continuing to receive batches under the automatic replenishment that RO_PID_42 requires.*

*On the two Wallet Unit grounds.* Revocation of a Wallet Unit and a report that one has been lost, stolen or compromised are distinct events with distinct triggers, and requirement VCR_07c makes the first a mandatory ground in its own right. A Wallet Unit may be revoked for reasons that involve no report from the User at all — among them the cancellation of its Wallet Provider, which requirement WPNot_06 in Topic 31 requires to be followed by revocation of every Wallet Instance that Provider issued.

*On out-of-band notification.* Requirement VCR_09 recommends that a PID Provider which has revoked a PID following a change of attribute values notify the User out of band, *if the User's contact details are known*, and ask them to request re-issuance. DGEP does not hold contact details for the Users of Romanian PIDs: RO_PID_09 declines to issue `email_address` and `mobile_phone_number` precisely because RNEP is not an authoritative source for either, and DGEP does not collect them by another route. The condition on which VCR_09's recommendation depends is therefore not met, and the notification path available to DGEP is the one this provision specifies. This is a consequence of the decision recorded in RO_PID_09 and is recorded here so that it is a stated position rather than an omission.

*A limitation follows and is recorded deliberately.* Notification is conditional on a consent the User is free to withhold. A technical PID remains in the Wallet Unit for up to two months after revocation, so a User who has declined notifications may hold what appears to be a valid PID for that period and discover otherwise only at the point of use — which, for a User relying on it to access a service, is the worst moment to find out. A Wallet Unit should therefore indicate the revoked status of a PID in its own interface, checking the status list published under RO_PID_56, rather than relying on notification alone. The drafting made this a duty rather than a recommendation, because it is the only means by which a non-consenting User learns of a revocation before attempting to use the PID.

## RO_PID_61 — DGEP SHALL review this Rulebook against the instruments on which it depends, as its author and…

*Why this Rulebook needs such a provision when the ARF does not require one.* Topic 12 imposes no obligation to maintain an Attestation Rulebook once written. That is tolerable for a Rulebook that defers to EU documents by reference, but this one does not: it is a self-contained profile that **restates** EU normative content so that an implementer need not read two documents in parallel. Restatement is what makes the Rulebook usable, and it is also what makes drift its principal failure mode. A Rulebook that quotes a requirement is wrong the moment that requirement changes, and nothing about the Rulebook will look wrong.

*Why clause (c) is not redundant.* A trigger-based obligation fails silently when nobody notices the trigger. The annual backstop is what catches a publication that passed unobserved.

*Why clause (e) matters more than it appears to.* A date that is refreshed only when something changed cannot be distinguished, by a later reader, from a date that was never revisited at all — the two look identical. Updating it unconditionally is what turns the baseline date in the version history from a disclaimer into evidence that somebody looked on that date and found nothing to change. The date is recorded in one place, so that two copies of it cannot disagree about when the assessment was last performed.

*Why clause (d) is not ceremony.* The defects a conformance assessment catches are the ones reading does not: a domestic namespace that does not conform to the requirement constructing it, or a citation to a requirement that no longer carries the obligation attributed to it. Neither looks wrong on the page, and neither surfaces unless somebody goes requirement by requirement. Clause (d) exists so that this happens without depending on anyone deciding to undertake it.

*Why Chapter 8 says what has been assessed and what has not.* An unqualified assertion of compliance offers a reader nothing to check. Annexes B and C are evidence of a different kind: a reader can take any requirement of Topic 3 or Topic 12, find the row, and check it against the provision named — and, where a withdrawn section transposed it, find it marked as not currently transposed. A Rulebook that made the bare claim and the evidenced one in the same voice would invite the first to be relied on as though it were the second, which is the failure clause (d) keeps this Rulebook out of.
