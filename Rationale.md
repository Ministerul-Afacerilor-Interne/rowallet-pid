# Rationale for the Romanian PID Rulebook

**Companion to `RO_PID.md`, the Romanian PID Rulebook. Accompanies version 0.1 of that document.**

**Author:** Ministerul Afacerilor Interne, Direcția Generală pentru Evidența Persoanelor<br>
**Version:** 0.1 — 31 Aug 2026<br>
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

**Sections 5.2 to 5.4 and the whole of Chapter 7 carry no content.** This document keeps their
reasoning. That is deliberate and is not an
oversight: the withdrawn text is retained by DGEP, and the argument for it is the thing most easily
lost between a decision being deferred and the same decision being taken a year later by different
people. A heading below for one of those provisions should be read as *why the
withdrawn text said what it said*, and as an input to settling the Annex D entry rather than as a
justification for anything currently in force.

**This document follows the Rulebook.** There is a heading below for every provision the Rulebook
states and for every identifier it reserves, in the order the Rulebook reads, save for three. RO_PID_42 and
RO_PID_49 were never separately explained. RO_PID_34 has no entry because the duty it once
carried — issuing to a Wallet Unit of every recognised Wallet Solution — is in force under
RO_PID_31, and the reasoning for it sits there. There is nothing for an attribute the Romanian PID
does not carry; Chapter 2 of the Rulebook records every attribute it declines, and the reason.

**"This Rulebook" below means `RO_PID.md`.** This document is not a Rulebook and states no
requirement of its own; where the phrase appears in the reasoning it refers to the document that
reasoning explains.

---

## RO_PID_01 — DGEP SHALL be the sole PID Provider of the Romanian PID.

*Why a single PID Provider.* DGEP holds RNEP and generates the CNP, so it is the only body in Romania that can attest the values a Romanian PID carries without reading them from somewhere else — which RO_PID_04 forbids. A second PID Provider would necessarily populate its attestations from a copy of the register, and where the two disagreed no Relying Party would have any means of telling which was authoritative. The prohibition on any other entity using the document type, the namespace or the Verifiable Credential Type is what gives those identifiers their meaning: a Relying Party that recognises `eu.europa.ec.eudi.pid.ro.1` knows, from the identifier alone, which authority stands behind the attributes.

*Why at most one logical PID per Wallet Unit.* Two logical PIDs in one Wallet Unit would attest the same person, from the same register, over two administrative validity periods running independently of one another. A correction applied to one would leave the other outstanding and looking correct, and the batch, replenishment and revocation rules would each have to say which of the two they meant. Nothing is gained in exchange: a Wallet Unit already holds many technical PIDs of one logical PID, and that is what makes repeated presentations unlinkable.

*Why the converse is left open, and said to be left open.* Whether one User may hold a logical PID in two Wallet Units — the case of a personal and a work device — is a question about the User rather than about the Wallet Unit, and this provision does not answer it. It turns on how identity proofing and revocation reach a second device, which belongs with the enrolment and lifecycle provisions. The Rulebook records the gap expressly rather than leave a reader to infer a prohibition from a rule that does not state one.

## RO_PID_02 — The Romanian PID SHALL be issued at level of assurance high, as defined in the European Digital…

*Why the level is stated in the Rulebook at all.* It follows from the European Digital Identity Regulation, which requires a Wallet Unit to be provided under an electronic identification scheme notified at level of assurance high; the PID is what carries the identity into that Wallet Unit, and a PID issued at a lower level would be the weakest link in a chain the Regulation requires to be strong throughout. Stating it here is nonetheless what makes RO_PID_31 legible. The enrolment process in that provision — an electronic step, then an in-person comparison of the User against their CEI and against the RNEP record — is not a national preference for ceremony; it is what [CIR 2015/1502] asks for at this level, and a reader who did not know the level would have no way of telling which parts of it are negotiable.

*What the level does not depend on.* It rests on the identity proofing DGEP performs, and not on the notification status of any Romanian scheme. RO_PID_31 records that separately, because the two are easily conflated and the second is outside this Rulebook's control.

## RO_PID_03 — DGEP SHALL issue every logical Romanian PID in both the format specified in [ISO/IEC 18013-5] and the…

*Neither encoding is optional and neither is a fallback for the other. Chapters 3 and 4 specify both because a Wallet Unit holds both: the [ISO/IEC 18013-5] encoding serves proximity presentation and the [SD-JWT VC] encoding serves remote presentation, and a User who held only one could not transact in the other setting.*

## RO_PID_04 — RNEP SHALL be the authoritative source for every PID attribute derived from civil-status or population…

*Why RNEP and not the CEI.* Both were candidates. The CEI carries a copy of some of the same values, itself derived from RNEP, and a scheme with no central register has no choice but to read from the card — which is why some Member States do. Romania has a central register, so the choice was real, and it matters because the two are known to **diverge in encoding**: a PID populated from the card would not always carry the same bytes as a PID populated from the register, and neither party to a mismatch would be able to say which was wrong. Reading from RNEP removes the question. The CEI is retained for what it is good at — proving at onboarding that the person in front of the counter is the person in the register — and is not a source of attribute values.

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

*The decisive point is that the multilingual slot already exists elsewhere in the stack.* Issuer and credential metadata are explicitly multilingual by design, whereas the attribute is a single string. Putting a second language in the attribute would be duplicating — badly, in one flat string — what the surrounding metadata does properly, one object per language. Four mechanisms carry the translation, each better suited than the attribute:

- **Credential Issuer Metadata** under [OpenID4VCI], published by DGEP. Its `display` parameter is an array with one object per language, each carrying a `name` and a `locale`. It is the most directly relevant mechanism, because every Wallet Unit that obtains a Romanian PID reads this metadata in the course of issuance. **No provision in force presently requires DGEP to publish it**, the provision that did being withdrawn with Sections 5.2 to 5.4; the duty to carry at least Romanian and English falls on the Type Metadata under RO_PID_29.
- **Type Metadata** under [SD-JWT VC], published by DGEP per RO_PID_29, whose `display` array carries per-language entries keyed by `lang`, covering the type and the domestic claims.
- **The Trusted List** published under [CIR 2024/2980], which carries the registered name of the PID Provider and supports multilingual name entries. It, not the attestation, is the authoritative record of who DGEP is. That list is the List of Trusted Entities of PID Providers, not a Trusted List; see RO_PID_53.
- **`issuing_country`**, fixed at `RO`, which already gives machine-readable provenance without any party needing to parse the authority name.

*Two traps for implementers,* both stated in the Rulebook. The language key differs between the first two: [OpenID4VCI] uses `locale`, [SD-JWT VC] Type Metadata uses `lang`. Both take a [BCP 47] language tag, so the values are interchangeable but the member names are not. And because the English name is published in two places, the two could drift — RO_PID_29 requires the English name in the Type Metadata to be identical to the one in the Credential Issuer Metadata, so that a Relying Party does not obtain two different English names for DGEP depending on which document it reads.

## RO_PID_13 — `expiry_date` SHALL be computed from `issuance_date`.

*Why the administrative validity is four years, and why it is computed rather than copied.* The obvious alternative is to take `expiry_date` from the CEI on which the logical PID was founded, on the reasoning that a PID should not outlive the document that proved the identity behind it. It is not used, because the link would carry two costs. It would make the administrative validity of a PID unpredictable — a CEI issued to a child runs four or five years, one issued to an adult ten, one issued over seventy has no expiry at all, so a fallback would have to invent a term anyway. And it would make the PID's lifetime depend on a document the User replaces for reasons of their own, so a routine card renewal would shorten or extend the attestation.

A fixed four-year term avoids both. Every logical PID has the same administrative validity, DGEP can compute it without reading the card, and the User's card renewal cycle and PID renewal cycle are independent of one another.

*Why four years, and not more.* The number is a national choice and nothing in the EU instruments constrains it — [PID Rulebook] says in terms that *"It is up to the PID Provider to decide whether the logical PID has an administrative validity period"*, and requirements PID_13 and PID_20 ask only that a policy exist relating these dates to the technical validity period, which RO_PID_14 supplies. Four years is short enough that the attribute values in a PID are re-established against RNEP at a reasonable cadence, and long enough that re-issuance is not a routine annoyance.

*Why the day before the anniversary.* RO_PID_14 provides that the administrative period runs from 00:00:00 on `issuance_date` to 23:59:59 on `expiry_date`. Setting `expiry_date` to the anniversary itself would make the period four years and one day. Taking the day before makes it exactly four years, which is what was decided.

*Why neither date carries a time.* [CIR 2024/2977] defines both as a date "and if possible time", and the permission is not taken. The administrative validity period is administered in whole days; a time of day would assert a precision DGEP does not have, and it would put a time zone into a value that has to mean the same thing to a verifier anywhere. What a date needs instead is a stated convention for the one case where it must be compared against an instant, and RO_PID_14 supplies it: Romanian local time, converted to UTC. A Relying Party that evaluated the two dates against its own local date could be a day out; the provision says not to. No equivalent question arises for `validFrom`, `validUntil`, `nbf` and `exp`, which carry absolute instants with the [RFC 3339] offset fixed at `Z`.

*What the CEI still does, and what it does not.* The identity proofing behind a Romanian PID is performed against a valid CEI at enrolment, under RO_PID_31. What the CEI does not fix is the attestation's administrative life, which is independent of that document's. Where a CEI is invalidated, cancelled or reported lost, that remains a matter for the revocation grounds in Chapter 7 rather than for the expiry date.

*On the distinction between the two validity periods. The technical validity period is a mandatory element of every technical PID and is much the shorter of the two; its length is not settled, and RO_PID_38 will fix it. It will be the batching and single-use rules to be settled at RO_PID_39, rather than that period, that limit the ability of malicious Relying Parties to track Users through the repeated presentation of the same attestation. The administrative validity period of the logical PID is measured in years. During it, DGEP provides successive technical PIDs to the Wallet Unit without any action being required of the User. When the administrative validity period ends, the User applies for a new logical PID.*

## RO_PID_14 — The relationship between the administrative dates and the technical validity period of a technical PID…

*Three hazards make this provision necessary rather than formal. A `full-date` has no time element while `validFrom` and `nbf` are UTC instants, so the two cannot be compared without a stated convention — and Section 3.1.2 requires `full-date` for both attributes, which makes the ambiguity live. A User shown an `expiry_date` still in the future must not be left holding no presentable PID, which the fifth clause addresses — the clause whose division of the duty is registered at **N8**. And where local law ties the administrative dates to those of a physical document, the policy must accommodate it. Romania's does not: RO_PID_13 computes `expiry_date` from `issuance_date` over four years and expressly forbids deriving it from the expiry of the CEI.*

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

*Why the cost of adding one is worth paying.* An amendment means a new version of this Rulebook, a new publication in the catalogue of attestation rulebooks under RO_PID_30, and a revised Type Metadata under RO_PID_29. That cost is the point. A domestic attribute is one no Relying Party outside Romania can be expected to interpret, and a domestic set that grew by increments would end in a Romanian PID that only Romanian Relying Parties could read — which is the outcome the EU-wide attribute set exists to prevent.

*Why these two.* The CNP, because Romania operates no identifier distinct from it and a PID carrying no persistent identifier could not support the processes that need one; the age assertions, because they are the minimising alternative to disclosing `birth_date`, and because age attributes left [PID Rulebook] at its version 1.1 and are therefore available only domestically. RO_PID_19 and RO_PID_20 carry the reasoning for each.

## RO_PID_19 — `personal_numeric_code` SHALL contain the CNP of record in RNEP: exactly thirteen decimal digits…

*Why the CNP is a domestic attribute, and the only identifier.* Romania operates no personal identifier distinct from the CNP and does not introduce one for the purposes of the PID. The CNP is carried as a domestic attribute, under its own name, so that a Relying Party requesting it does so knowingly. It is the only unique, persistent identifier a Romanian PID carries: a Relying Party that needs to identify a User across presentations has no alternative attribute available to it, and one that does not need to should request no identifier at all.

*The legal basis.* The CNP is established by Article 6 of [OUG 97/2005], which at paragraph (2) defines it as a *significant number that uniquely individualises a natural person* and at paragraph (3) provides that it is generated by DGEP. Article 6(1) of that instrument, with Article 22(1) of [Law 119/1996] on civil status documents, provides that it is assigned from birth. The Rulebook cites the instruments rather than restating the definition, because the definition is the legislature's and may be amended without reference to this document.

*Why the first digit is constrained, and to 1 to 6.* The first digit encodes the sex and the century of birth, and its range depends on who assigns the CNP. RNEP assigns 1 to 6 to Romanian citizens, which is the population this Rulebook governs; 7 and 8 are assigned to foreign nationals, whom this version does not reach. The range is stated on that basis and not inferred, because a PID Provider validating the digit on a guess would reject a lawfully assigned CNP. **If the scope of the Rulebook ever extends beyond Romanian citizens, this is one of the provisions that moves with it.**

*A CNP is not immutable.* It is reassigned in exceptional circumstances — a material error in the civil-status record, a legal rectification of the date of birth, an official change of gender. The Rulebook does not describe the CNP as permanent for that reason. The machinery that will handle the change is the subject of two reserved provisions: RO_PID_43 will govern the re-issuance of technical PIDs whose values have been superseded, and RO_PID_60 the grounds on which an uncorrectable change causes the logical PID to be revoked.

*What disclosing the CNP entails.* The thirteen digits are structured `S AA LL ZZ JJ NNN C`: a sex-and-century digit, the year, month and day of birth, the county of registration, a sequence number, and a check digit. The CNP is therefore a *speaking* identifier. A Relying Party that obtains it obtains the User's sex, full date of birth, and county of registration as well — three attributes it may not have requested, in circumstances where the presentation interface would show only that a single number was being shared. Naming the attribute for what it is, rather than as a generic administrative reference, is what allows a Relying Party — and particularly one established in another Member State — to recognise what it is asking for. That name is what makes the disclosure visible to the party consenting to it; the request restriction to be settled at RO_PID_50 and the display obligation at RO_PID_47 will reinforce it.

## RO_PID_20 — `age_equal_or_over` SHALL assert, for each of the age thresholds 14, 16, 18 and 65, whether the User…

*Why the PID carries age assertions when it already carries a date of birth.* A Relying Party that needs to know whether a User is old enough for something needs one bit, and `birth_date` gives it that bit only by also giving the User's exact age, birthday and star sign, none of which the Relying Party asked for or may lawfully retain. An age assertion is the minimising alternative: a Relying Party requesting `age_equal_or_over.18` learns whether the User is an adult and learns nothing else. The thresholds are carried as separate assertions rather than as a single age so that this holds for each of them independently.

*Why all four are always present.* If DGEP issued only the assertions that happened to be true, the set of assertions present would itself disclose the User's approximate age to anyone who received any one of them. Issuing all four, true or false, means the presence of an assertion carries no information and only its disclosed value does.

*Why these four.* Each of the four has an identified use, and no other threshold does. A threshold that no Relying Party requests is not free: it is an additional attribute in every attestation, an additional digest in every Mobile Security Object, and an additional date on which the technical validity period will have to be truncated once RO_PID_38 fixes it.

*Age assertions in the PID are attributes of the PID.* They are defined under PID_06 as domestic attributes, age attributes having left [PID Rulebook] at its version 1.1. Romania does not operate a separate electronic attestation of age.

## Chapter 3 — why the [ISO/IEC 18013-5] encoding is mandatory, and not merely offered

Requirement ARB_02 in Topic 12 in Annex 2 of the ARF obliges the author of an Attestation Rulebook to analyse whether a User must be able to present the attestation while in proximity to the Relying Party and without using the internet, and, if so, to require the [ISO/IEC 18013-5] format. **The analysis itself is in the Rulebook, at the opening of Chapter 3**, which is where ARB_02 requires it and where Annex C claims conformance for it; what follows here is why it came out as it did. A Romanian PID is the electronic counterpart of the CEI, and the transactions in which a CEI is presented today are overwhelmingly face-to-face: identification at the counter of a public authority, at a bank, at a notary, in a hospital, and in the course of a police check. In many of those settings the User has no connectivity, the Relying Party has none, or neither does. A Romanian PID that could be presented only over the internet would not serve the purpose for which it is issued. Both encodings are accordingly mandatory under RO_PID_03, and this one is what makes proximity presentation possible.

## RO_PID_21 — An [ISO/IEC 18013-5]-compliant Romanian PID SHALL use the document type `eu.europa.ec.eudi.pid.1`, as…

*The identifier of the domestic namespace is not freely chosen. PID_06 requires it to be generated by appending the [ISO 3166-1] alpha-2 country code, separated by a period, to the namespace identifier of PID_05 with the version number excluded, optionally followed by a version number. For Romania that yields `eu.europa.ec.eudi.pid` + `.ro` + `.1`. A reverse-domain identifier under a national domain would satisfy the uniqueness requirement of ARB_06a in Topic 12 but would still breach PID_06, because PID_06 constrains the construction and not merely the uniqueness of the result.*

## RO_PID_22 — Every domestic attribute SHALL be carried in the `eu.europa.ec.eudi.pid.ro.1` namespace.

*Note on `resident_house_number`.* [PID Rulebook] defines this attribute only as a member of the `address` structure of the [SD-JWT VC] encoding. It has no attribute identifier in the [ISO/IEC 18013-5] encoding, and this Rulebook does not create one, since doing so would require adding an attribute to the `eu.europa.ec.eudi.pid.1` namespace, which is not within the competence of a national Rulebook. The question does not arise for a Romanian PID in either encoding: RO_PID_11 declines `resident_street` and `resident_address` along with every other address attribute, so there is no structure for a house number to sit in.

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

*The encoding of an empty portrait is prescribed by PID_03 in Topic 3 in Annex 2 of the ARF and is not a national choice. Stating it explicitly matters because "empty" admits of at least four implementations — a zero-length `bstr`, an empty string, an empty data URL, and an absent attribute — which would not interoperate. Note also that PID_03 leaves the offering of the opt-out to the discretion of the PID Provider; this provision requires DGEP to offer it to every User, which is stricter and is permitted.*

*Whether a User can change their mind, and what it costs.* They can, and the machinery that carries it already exists. A technical PID is signed and cannot be edited, so any change of election takes effect on the next technical PIDs issued — which is re-issuance, the process Topic 10 in Annex 2 of the ARF already requires DGEP and RO Wallet to support over [OpenID4VCI] (ISSU_63, ISSU_65) and already requires RO Wallet to offer the User a means of starting (ISSU_58). ISSU_62 is written for exactly this case: a technical PID re-issued *because an attribute value changed, including an attribute being added or deleted*. The Wallet Unit stops presenting the superseded technical PIDs and deletes them.

*And the outstanding technical PIDs are revoked — but not all of them.* VCR_09 is narrower than it first reads. It bites only where the attestation **is revocable**, only where the value of an attribute of the corresponding **logical** PID changed, and only on a technical PID **still valid for at least 24 hours**; one closer to expiry than that is left to expire. RO_PID_25 states all three limbs rather than the bare duty, because the bare duty would have been read as revoking a whole outstanding batch in every case. The revocability limb is not academic either: whether a Romanian technical PID is revocable at all is Chapter 7's question, and Chapter 7 is withdrawn.

*Where the discretion sits, and why it is worth having.* Revocation follows from DGEP **applying** the changed election, not from the User asking. That distinction is the only thing standing between a display preference and a revocation storm: the portrait election is the one attribute value a User can change at will, and a User who toggles it repeatedly would otherwise force a full batch revocation and re-issuance each time — a status-list write per outstanding technical PID, on infrastructure sized for name changes and deaths. RO_PID_25 therefore permits DGEP to apply the change at the next replenishment. Nothing is lost by the delay: throughout it the User holds a PID whose portrait is empty, which is what they had before, and phase 1 carries an empty portrait for every User in any event.

*Why no new logical PID is needed.* Re-issuance continues the same logical PID in the same Wallet Unit — that is what ISSU_65's same-Wallet-Unit check is for. The administrative validity period is untouched, so `issuance_date` and `expiry_date` do not move and the four-year term of RO_PID_13 does not restart. Requiring a new logical PID would have been the wrong answer twice over: it would restart a term for a reason unrelated to identity, and it would force the User back through the enrolment of RO_PID_31 to change a display preference.

*Why the Rulebook has to say so.* PID_03 places the opt-out "during issuance of a PID" and stops there. It neither provides for a later change nor forbids one, so a Wallet Provider building the setting has nothing to build against and DGEP has no stated obligation to honour a request. The paragraph added to RO_PID_25 supplies the election and its reversibility; everything downstream of it was already mandatory.

*On timing.* [CIR 2024/2977] makes the inclusion of `portrait` mandatory as of twenty-four months after the entry into force of the Regulation amending it. This Rulebook requires the **attribute** from the first issuance of a Romanian PID, ahead of that date, and its **value** from the date DGEP announces. The attribute is therefore mandatory throughout, and never optional and never absent; what the transitional rule in RO_PID_24 defers is the image and not the slot.

## RO_PID_26 — In a [SD-JWT VC]-compliant Romanian PID, all claims SHALL be individually selectively disclosable…

*The claims [SD-JWT VC] excepts are those whose function is to establish the validity, type, or key binding of the attestation itself rather than to convey an attribute. They are not enumerated in the Rulebook, so that it does not go stale if that list changes. `iat` is excepted by RO_PID_26 itself and not by the specification, which leaves it disclosable at the issuer's option: it dates the technical PID rather than saying anything about the User, so it shares the character of the rest and nothing is gained by hiding it behind a digest that every verifier would resolve.*

## RO_PID_27 — The `age_equal_or_over` claim SHALL be a JSON object whose members are the age thresholds defined in…

*Why the member names are strings and not numbers.* A JSON object key is a string by definition, so `{"14": true}` is the only well-formed rendering and `{14: true}` is not JSON at all. The provision says so because a list of thresholds written `14, 16, 18 and 65` reads as a list of integers, and an implementer working from that list rather than from the example could reasonably produce the second form. The [ISO/IEC 18013-5] encoding gives no help here: there the threshold is part of an attribute identifier, `age_over_14`, and the question does not arise.

*Why a Relying Party may not rely on the ordering.* Nothing in JSON fixes the order of object members, and two conforming serialisers may differ. The point is sharper here than it would be elsewhere, because RO_PID_26 makes each member individually disclosable: a Relying Party frequently receives one member and not the set, so a verifier reading the members positionally would be reading a structure it has not been given. It would also break the first time a threshold was added by amendment.

*Why all four are present whether true or false.* The reasoning is RO_PID_20's — the presence of an assertion must carry no information, or the set of assertions present would itself disclose the User's approximate age. It is restated in this provision because the object form makes omitting a false member the natural implementation, in a way that four separate attributes do not.

## RO_PID_28 — A [SD-JWT VC]-compliant Romanian PID SHALL use the Verifiable Credential Type `urn:eudi:pid:ro:1`.

*Why a domestic type rather than the base type.* `urn:eudi:pid:1` describes the EU-wide PID, which carries neither the CNP nor the age assertions. A Romanian PID presented under the base type would carry claims that type does not declare, and its Type Metadata could not describe them without ceasing to be the metadata of the base type. Requirement PID_14 provides for exactly this case, and this provision takes it.

*Why the type extends rather than replaces.* Extension preserves every mandatory claim of the base type, so a Relying Party that needs nothing domestic can process a Romanian PID against `urn:eudi:pid:1` and never learn that a domestic type exists. A separate, unrelated type would oblige every Relying Party in the Union to learn a Romanian type before it could read a family name, which is the interoperability cost the base type exists to avoid.

*Why the identifier takes this form.* PID_14 requires every PID type to sit in the `urn:eudi:pid:` namespace, and `urn:eudi:pid:ro:1` carries the [ISO 3166-1] alpha-2 country code in the same position, and to the same effect, as the `.ro` in the domestic namespace of RO_PID_21. The two encodings therefore identify Romania in the same way, which is one fewer thing for an implementer building both to remember.

## RO_PID_29 — DGEP SHALL author and publish Type Metadata for `urn:eudi:pid:ro:1`.

*The duty falls on DGEP and not on DGCTI. The Type Metadata describes the attestation type — what claims it carries, what each means, how each displays — which is the PID Provider's subject matter and not the Wallet Provider's; and RO_PID_29 requires the English name it carries to match the one in the Credential Issuer Metadata, which DGEP publishes. The same reasoning puts the catalogue entry in RO_PID_30 on DGEP.*

*Requirement ARB_31 in Topic 12 in Annex 2 of the ARF recommends this. It is made mandatory here because RO_PID_26 states the disclosability rule once, in prose, for every claim at once; without the corresponding machine-readable metadata a Wallet Unit implementer has nothing to build against, and the general rule would have to be re-derived by hand for each claim. The two are required to agree, and where they do not, RO_PID_26 governs and the Type Metadata is corrected.*

## RO_PID_30 — DGEP SHALL publish this Rulebook in the catalogue of attestation rulebooks, complying with the…

*The two catalogues are distinct and serve different readers. The catalogue of attestation rulebooks holds this document, which is human-readable; the catalogue of attestation schemes holds a machine-readable description of the same attestation. ARB_33 exists so that a party who finds the scheme can reach the Rulebook that explains it.*

*Requirements PID_07 and PID_16 in Topic 3 require a PID Provider that defines a domestic namespace or a domestic type to publish it — with all attribute or claim identifiers, their definitions, presence and encoding format — in an Attestation Rulebook complying with Topic 12. This Rulebook is that Attestation Rulebook, and Sections 2.7, 3.1.5 and 4.1.3 are that publication; see Chapter 8. Publishing it in the catalogue is what makes it reachable by a Relying Party in another Member State, which is the point of the requirement: without it, such a Relying Party encountering a Romanian PID has no documented means of discovering what the domestic namespace contains.*

## RO_PID_31 — DGEP SHALL issue a logical Romanian PID only after identity proofing and verification meeting the…

*Why the process is one channel and not two.* Two independent routes are conceivable — enrolment in person at a counter, or remotely with the CEI read over its contactless interface — and neither alone is sufficient. The remote step establishes that the applicant **possesses the CEI and knows its PIN**; the counter step establishes that the **person present is the person the card and the register describe**, which a contactless read cannot do. Assurance level high under [CIR 2015/1502] wants both, and the process combines them rather than offering a choice between them.

*What the two scans are for, and why they are not ceremony.* The identity checks at the counter establish who the User is. They do not establish **which device receives the attestation**, and without that a PID could be issued to a Wallet Unit other than the one that began the enrolment — the failure mode activation exists to prevent. The first scan binds the counter session to the Wallet Unit that read the CEI; the second, over a code that lives for less than a minute, records the User's authorisation to issue while they are still present. That is why RO_PID_32 identifies these steps as the activation process rather than adding a separate one.

*On the assurance level, and what the CEI is doing here.* The Romanian electronic identification scheme is not notified at level of assurance high, and nothing in this Rulebook requires that it be. The electronic step establishes possession of the CEI and knowledge of its PIN; it is evidence of possession, not the use of a notified electronic identification means, and nothing in this Rulebook turns on the notification status of any scheme. The level of assurance in RO_PID_02 rests on the identity proofing — the comparison of the person present against the card and against the RNEP record, at the counter — which is what [CIR 2015/1502] Section 2.1.2 asks for and which does not depend on notification at all. A prohibition on issuing against an electronic identification means below high would describe a route this process does not use, and this Rulebook states none.

*Why the second code is short-lived.* A QR code that stayed valid would be a bearer token for issuing a PID: photographed at the counter, it could be scanned later by another device. Refreshing it every few seconds and expiring it inside a minute makes the authorisation useless the moment the User leaves.

*Why the duty reaches every recognised Wallet Solution, and not only RO Wallet.* This is the paragraph of the provision with the widest practical reach. RO Wallet is the Wallet Solution provided by the Ministry, and the rest of this Rulebook is written with it in view, but nothing in the European Digital Identity Regulation confines a Romanian PID to it: a Wallet Unit of any Wallet Solution recognised under the notified scheme is entitled to one, and DGEP publishes the list of those it accepts so that a prospective User can find it. Any condition DGEP applies at issuance is a condition about trust and revocation status, not about the identity of the Wallet Provider, and none of it is to be read as a preference for RO Wallet.

*Whether the process had to be in the Rulebook at all.* It did not. No requirement of Topic 3, Topic 12 or the Attestation Rulebook template asks a Rulebook to describe enrolment, and ISSU_05 binds the Wallet Unit to support activation rather than this document to specify it. It is here because a phase 1 draft that said nothing about how a citizen obtains a PID would be a draft nobody could evaluate, and because the process is a single combined channel — an unusual enough shape that leaving it unwritten invites it to be remembered as the two independent ones it replaced.

## RO_PID_32 — RO Wallet SHALL support a process to activate a newly issued Romanian PID, in accordance with the…

*Why activation is not a separate ceremony.* ISSU_05 requires a Wallet Unit to support a process to activate a newly issued PID in accordance with [CIR 2015/1502] Section 2.2.2, and that Section states an outcome — the attestation reaches the Wallet Unit and the secure device of the person who is its subject — rather than a procedure. Romania had to choose one. The choice made is to identify activation with steps 5 to 9 of RO_PID_31 rather than to add a step after issuance.

*Why that is the better answer.* An activation performed after issuance has to re-establish something already established minutes earlier at the counter, and every re-establishment is another chance to get it wrong. The two scans already prove that the device completing the enrolment is the device that started it and that the User authorised issuance from it in person. Adding a further step would satisfy the wording of ISSU_05 while delivering nothing the process had not already delivered, which is the no-op the requirement exists to prevent rather than to produce.

**The entries below explain provisions that carry no content.** Their identifiers are reserved in
version 0.1 and the text they once explained is held by DGEP. They are kept because the argument for a
deferred design is the thing most easily lost between a decision being put off and the same decision
being taken later by different people. **None of them states a requirement**, and an implementer
building to any figure or rule mentioned in them is building to something the Rulebook does not say.

| Reserved for | Identifiers | Settles with |
|---|---|---|
| Sections 5.2 to 5.4 — issuance, lifecycle, presentation, restrictions on requesting | RO_PID_33 to RO_PID_52 | **N12** |
| Chapter 7 — revocation | RO_PID_56 to RO_PID_60 | **N13** |

---

## RO_PID_33 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_33 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the issuance protocol.

*This is where the multilingual name of the PID Provider belongs. The `display` array of the Credential Issuer Metadata holds one object per language, so it can carry the authority name in as many languages as are useful, whereas the `issuing_authority` attribute is a single string and can carry only one. RO_PID_12 keeps the attribute in Romanian for that reason; this provision is what makes an English name available to a Wallet Unit or Relying Party that needs one.*

*This transposes requirements ISSU_64 and ISSU_63 in Topic 10 in Annex 2 of the ARF, and it is stated because the rest of this Rulebook assumes both without ever requiring either. RO_PID_39 obliges DGEP to issue in batches, RO_PID_42 obliges it to replenish them automatically and RO_PID_44 obliges it to publish the batch size — none of which is possible unless the protocol feature carrying a batch is implemented. Re-issuance is required by RO_PID_46.*

*Terminology.* Annex 1 of the ARF uses **Wallet Unit Attestation (WUA)** as the umbrella term and defines two concrete subtypes: the **Wallet Instance Attestation (WIA)**, which attests the integrity and authenticity of the Wallet Instance, and the **Key Attestation (KA)**, which attests the certification and properties of the Wallet Secure Cryptographic Device and carries the public keys it holds. Requirement ISSU_21 requires both to be verified and requires two distinct revocation checks, one on the Wallet Instance and one on the device. A provision requiring only "a valid Wallet Unit Attestation" would leave it open which of the two was meant, and would not reach the device at all.

*On what the verification is performed against.* Topic 9 in Annex 2 of the ARF, and not Topic 10, is where the two attestations are defined and where most of a PID Provider's duties in respect of them are stated. Requirement WUA_25 fixes the verification of the Wallet Instance Attestation to Appendix E of [OpenID4VCI] and WUA_11a fixes the verification of the Key Attestation to Appendix F.4, each adding the requirement to validate that the attestation is not revoked; WUA_36 binds a PID Provider to [Technical Specification 3]. A requirement to "verify" an attestation without stating the procedure is not implementable by an independent party, which is why the two Appendices are named here.

*The by-value rule is requirement RPRC_22 in Topic 44 in Annex 2 of the ARF, and the reason for it is that a Wallet Unit must be able to validate DGEP without making a further request to a third party: an issuance transaction is to be atomic and self-contained. A by-reference implementation would satisfy the sentence preceding it and fail the ARF. The distribution rule is requirement RPRC_14; a service supply point that does not hold the certificate cannot issue, because RO_PID_33 requires a conforming Wallet Unit to refuse where it cannot find one.*

*This transposes requirements ISSU_22, ISSU_24a and ISSU_24b. The last two are addressed to the Wallet Unit rather than to DGEP: before requesting issuance, a Wallet Unit inspects those two members and, if either check does not confirm the registration, warns the User and does not request a PID. They are stated here because the obligation they create for DGEP is implicit but absolute — a Wallet Unit that cannot find a valid registration certificate in the metadata is required to refuse, so a DGEP deployment that omits one cannot issue a PID to any conforming Wallet Unit.*

## RO_PID_35 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_35 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the Wallet Provider's duty to make RO Wallet capable of requesting issuance.

*This transposes requirements ISSU_23a and ISSU_23b. It is stated for completeness of the Wallet Provider's obligations under this Rulebook; DGEP is at present the sole PID Provider of the Romanian PID under RO_PID_01.*

## RO_PID_36 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_36 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns device binding and the keys a technical PID is bound to.

*These three limbs transpose requirements WUA_09a, WUA_12 and WUA_34 in Topic 9 in Annex 2 of the ARF. They are not a restatement of one another. Binding to a key the Key Attestation does not attest would leave the device unproven; proof of possession of the single key being bound would leave the remaining attested keys unaccounted for, which is what WUA_12 closes for a batch issued under RO_PID_39; and neither establishes, without WUA_34, that the attested keys are held where the Key Attestation says they are.*

## RO_PID_37 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_37 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns whether the attestation is device-bound.

*Requirement ARB_34 in Topic 12 in Annex 2 of the ARF obliges an Attestation Rulebook to state whether its attestation is device-bound. The answer here is not in doubt — device binding is called 'mdoc authentication' in [ISO/IEC 18013-5] and 'key binding' in [SD-JWT VC], requirement ISSU_17 makes it mandatory for every PID, and RO_PID_36 already requires it — but ARB_34 asks for the statement and not for the inference.*

*On the second paragraph.* Requirement ARB_28 permits a Rulebook to define a `cryptographically_bound_to` attribute recording that the Attestation Provider requested a cryptographic binding between the new attestation and an existing PID or attestation at issuance. That mechanism exists so that a subordinate attestation can be tied to the PID that identified its subject. The PID is the attestation others are bound **to**; there is nothing above it in that relationship for it to be bound to in turn.

## RO_PID_38 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_38 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the length of the technical validity period.

*On the age constraint.* `age_equal_or_over` is the only attribute of a Romanian PID whose value changes on a date DGEP can compute exactly and in advance, and it changes for every User who reaches 14, 16, 18 or 65 — the four thresholds RO_PID_20 fixes, and the only four, since it forbids an assertion at any other. Without this constraint, a technical PID issued shortly before such a birthday would continue to assert that the User had **not** attained the threshold for as long as two months after they had, and RO_PID_43 would oblige DGEP to revoke it — turning every threshold birthday in the country into a revocation event. Truncating the technical validity period so that it ends before the birthday means the situation cannot arise: the assertions in a technical PID are true for the whole of its technical validity period, by construction. The cost is that a User approaching a threshold receives shorter-lived technical PIDs for a time, which RO_PID_42 replenishes automatically and the User does not see.

*The second constraint transposes requirement ISSU_12c in Topic 10 in Annex 2 of the ARF. Its purpose is that a technical PID should not outlive the assurance on which it was issued: the Wallet Instance Attestation and the Key Attestation are what tell DGEP that the Wallet Instance is genuine and that the private key is held in a certified device, and each is maintained for a bounded period. A technical PID still presentable after that period rests on an assertion nobody is any longer maintaining. The constraint has real work to do at a two-month technical validity period, where it would have bound rarely at a period of hours.*

*A technical PID valid for two months is not a short-lived attestation within the meaning of requirement VCR_01 in Topic 7 in Annex 2 of the ARF, which sets that threshold at 24 hours or less. The Romanian PID is therefore a revocable attestation, and the revocation machinery in Chapter 7 is not a precaution but the sole means by which an incorrect or withdrawn PID is taken out of circulation. Two provisions carry that weight: RO_PID_58, which cascades revocation of a logical PID to every unexpired technical PID derived from it, and RO_PID_59, which bounds how stale a Relying Party's view of revocation status may be.*

## RO_PID_39 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_39 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns batch issuance and the size of a batch.

*The two requirements in the first paragraph are not in tension, and requirement ISSU_11a obliges a Wallet Unit to verify the first of them. "Distinct" here means distinct as an attestation — a different key pair, different salts, different attribute digests and a different issuer signature — and not distinct in content. Two technical PIDs of the same batch attest exactly the same facts about the same User; what must differ is everything by which a Relying Party could recognise one presentation as involving the same attestation as another. RO_PID_41 states which elements those are.*

## RO_PID_40 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_40 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns replenishment when a Wallet Unit runs out.

*Batching with single use is what denies Relying Parties a correlator. If a Wallet Unit presented one attestation repeatedly, colluding Relying Parties could correlate those presentations by the attestation itself, regardless of which attributes the User disclosed. A fresh attestation with a fresh key for each presentation removes that correlator.*

*This provision bears that burden alone. The technical validity period in RO_PID_38 does not constrain correlation over an interval of two months, so the batch size and the single-use rule are the whole of the measure. The minimum of 5 is a floor and not a target: the operative batch size is an operational parameter, published under RO_PID_44 rather than fixed here.*

*This provision transposes requirements ISSU_46 and ISSU_47 in Topic 10 in Annex 2 of the ARF, which govern the fall-back from Method A to Method B. The exception is narrow and is not a relaxation of RO_PID_39: it applies only when the alternative is that the User cannot present their PID at all. The ARF resolves that conflict in favour of the User being able to transact, and RO_PID_39 is drafted subject to it rather than against it.*

## RO_PID_41 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_41 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the uniqueness of per-attestation elements.

*Why the third paragraph is not satisfied by the second.* The elements listed above are values DGEP chooses and can therefore make unique. A timestamp is not chosen — it is observed — and the natural implementation, stamping every technical PID in a batch with the instant the batch was assembled, produces a value that is identical across the batch and almost certainly unique to it. That is a batch identifier in all but name. Note the interaction with RO_PID_38 and RO_PID_39: the technical *validity period* must be identical across a batch, so what this paragraph constrains is the issuance instant and any other timestamp, not the validity dates.

*Why the discard obligation matters to DGEP and not only to the User.* Retaining the per-attestation salts and digests would leave DGEP holding, in one place, the means to link every presentation of every Romanian PID ever made. The PID Provider is the one party in the ecosystem that could construct such a record, and this provision is what puts it beyond reach.

*This provision transposes requirements ISSU_35, ISSU_35b and ISSU_36 in Topic 10 in Annex 2 of the ARF, and is the operative content of requirement ARB_22 so far as the privacy of the Romanian PID is concerned. It completes what RO_PID_39 begins. Rotating attestations achieves nothing if the attestations carry a value in common: two colluding Relying Parties comparing an identical attribute digest, an identical signature, or an identical revocation index would link the two presentations exactly, without needing any attribute the User disclosed.*

## RO_PID_43 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_43 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns when attribute values must be valid.

*Correctness at issuance does not by itself bound staleness.* A technical PID issued the day before a change of surname is recorded in RNEP carries the superseded name for the remainder of its two months, and nothing about the moment of issuance removes it from circulation. Bounding staleness therefore requires DGEP to detect the change in RNEP and act on it, which is what the second clause of this provision and Chapter 7 exist to do.

*It also completes RO_PID_60. That provision permits revocation where a change in RNEP has rendered an attested attribute incorrect and the PID cannot be reissued with the corrected value; this provision governs the ordinary case, where it can.*

*This provision transposes requirements PID_12 and PID_19 in Topic 3 in Annex 2 of the ARF.*

*The 24-hour threshold in that clause is taken from requirement VCR_09 in Topic 7 in Annex 2 of the ARF, which obliges a PID Provider to revoke a technical PID whose attribute values have changed where that PID is still valid for at least 24 hours. Below that threshold revocation achieves little, because the process of revocation may itself take up to 24 hours and the attestation would expire first. Above it — which, at the technical validity period set by RO_PID_38, means nearly every outstanding technical PID — revocation is mandatory, and DGEP has no discretion to let a value it knows to be superseded remain in circulation.*

*Operational consequence of the two-month period.* A batch is ordinarily exhausted by presentation rather than by the passage of time. Two consequences follow, and the design of RO Wallet has to account for them.

First, **the batch size is the binding constraint on availability.** A User who exhausts a batch has no unused technical PID for the remainder of the period. RO_PID_42 requires replenishment to be automatic, and a Wallet Unit that replenishes opportunistically whenever connectivity is available, rather than waiting until its supply is spent, avoids the failure; but the size of the batch, not the frequency of replenishment, is what determines whether a User runs out. A Wallet Unit retains presentable technical PIDs across long periods without connectivity, so proximity presentation is not constrained by the technical validity period.

Second, **the number of technical PIDs outstanding at any moment is large**, and the status lists published under RO_PID_56 are correspondingly large.

## RO_PID_44 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_44 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the issuance method and the publication of the batch size.

*This provision transposes requirements ISSU_39, ISSU_39a, ISSU_40 and ISSU_40a, and the second sentence of ISSU_45. Method A is what RO_PID_39 already describes; naming it, and publishing it where a Wallet Unit can read it, is what the ARF requires in addition. The batch size and the lower limit are published rather than fixed in this Rulebook because they are operational parameters that DGEP must be able to adjust without an amendment; RO_PID_39 is where the floor of 5 sat, beneath which the published size could not fall.*

*Requirement ISSU_38 obliges a PID Provider to fix the technical validity period and the batch size by a documented policy resting on a linkability risk analysis. That policy is DGEP's and sits outside this Rulebook, which is why the Rulebook fixes a floor and leaves the operative figure to be published.*

## RO_PID_45 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_45 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns re-issuance and how it differs from replenishment.

*This provision transposes requirements ISSU_58, ISSU_65, ISSU_59, ISSU_62 and ISSU_60 in Topic 10 in Annex 2 of the ARF, in that order.*

*Why it is stated separately from replenishment.* RO_PID_42 makes replenishment automatic and invisible, which is right for what it does: it hands the Wallet Unit more copies of a logical PID whose content has not changed. Re-issuance is the other case, and it needs the opposite properties. The User initiates it, or a change in RNEP forces it under RO_PID_43; the attribute values may differ from those already held, so the second and third rules exist to let the User see that they have; and it must not silently move a PID onto a different Wallet Unit, which is what the second rule prevents. Treating the two as one process would mean either that a corrected PID arrives without the User being told anything changed, or that obtaining an ordinary batch interrupts them.

*On the second rule.* ISSU_65 is the only limb of this provision addressed to DGEP rather than to RO Wallet, and it is the one with a security consequence: without it, a party who obtained the credentials of a re-issuance request could have a fresh Romanian PID delivered to a device that is not the User's. Section 14.5 of [OpenID4VCI] describes the mechanism the ARF contemplates — a device-bound refresh token issued at first issuance and required at re-issuance — and DGEP's implementation of RO_PID_33 has to provide for it.

## RO_PID_46 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_46 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns deletion of a Romanian PID from a Wallet Unit.

*The rules of this provision transpose requirements PAD_01, PAD_02, PAD_03, PAD_04 and PAD_05 in Topic 51 in Annex 2 of the ARF. The second matters more here than it would elsewhere: because RO_PID_39 puts a batch rather than a single attestation into the Wallet Unit, deleting "the PID" is ambiguous unless the Rulebook says which, and a deletion that left unused technical PIDs behind would leave presentable attestations in a Wallet Unit the User believes no longer holds any.*

*The fifth rule is not in Topic 51 and is required by the interaction between two provisions that are.* RO_PID_42 requires replenishment to be automatic, to require no action by the User, and to continue "for as long as the logical PID is valid and not revoked". Deletion satisfies neither of the conditions that stop it: the logical PID remains valid, and it is not revoked. PAD_03 then forbids the Wallet Unit to tell DGEP anything about the deletion, so DGEP cannot stop replenishing on its own initiative and must not be expected to. Without this rule the conforming behaviour would be for the Wallet Unit to delete the PID at the User's request and silently obtain a fresh batch of it, which is the opposite of what the User asked for. The obligation is therefore placed on the Wallet Unit, which is the only party that knows.

*On what deletion is not.* It is a decision by the User about their own device, not a statement about the validity of the PID. DGEP is not told, no status list changes, and the logical PID remains valid for the remainder of its administrative validity period — so a User who deletes and later re-applies is not treated as a new subject. This is also why deletion appears here and not in Chapter 7.

## RO_PID_47 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_47 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns what a Wallet Unit may present.

*These two paragraphs transpose requirements RPA_08 and RPA_07c in Topic 6 in Annex 2 of the ARF. The second is the only point at which the ARF imposes a SHALL on what a Wallet Unit must show a User about a particular PID attribute, and the Romanian PID carries the attribute it concerns. It sits alongside, and is stricter than, the recommendation in RO_PID_19 about the CNP: a portrait is biometric data within the meaning of Union data protection law, and RO_PID_52 governs what the Relying Party may do with it once obtained.*

## RO_PID_48 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_48 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns proximity presentation and the prohibition on server retrieval.

*The first paragraph transposes requirements ProxId_01, ProxId_01a and ProxId_05 in Topic 24 in Annex 2 of the ARF, and the second transposes ProxId_02, which is addressed to PID Providers by name.*

*Why the prohibition matters more to a PID than the requirement does.* Under server retrieval a Relying Party does not obtain attributes from the Wallet Unit at all: it presents a token received from the Wallet Unit to the issuer and obtains the attributes directly from it. For a Romanian PID that would mean DGEP learning the identity of every Relying Party the User transacts with, and the time of every transaction — the issuer-side observation that the whole design of Chapter 5 exists to prevent. RO_PID_41 discards the per-attestation elements by which DGEP could reconstruct a linkage record after the fact; server retrieval would hand DGEP the same picture prospectively and by design. The prohibition is therefore not an interoperability preference but the counterpart in Chapter 5 of what RO_PID_41 does in issuance and RO_PID_57 in revocation.

*The proximity analysis required by ARB_02 is recorded in the opening of Chapter 3. This provision is the mechanism by which the conclusion of that analysis is implemented.*

## RO_PID_50 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_50 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns when the national identification number may be requested.

*What this provision does.* It states the condition on which a Relying Party may request the national identification number. RPRC_21, which warns a User where a request exceeds the attributes a Relying Party registered, operates on the registered attribute set and is not the route by which this provision takes effect; the condition here is one a Relying Party applies to itself, and the general law applies to it independently.

*Why that matters more here than it would elsewhere.* The CNP is the only persistent identifier a Romanian PID carries, so every request for persistent identification lands on it, and it is a *speaking* identifier — a Relying Party that obtains it obtains the User's sex, date of birth and county of registration as well. That is why the provision is drafted as a condition on the request rather than as a preference, and why it works together with the display obligation in RO_PID_47, which is what makes the disclosure visible to the User approving it.

*The CNP is not merely an identifier. Its thirteen digits encode the User's sex, full date of birth, and county of registration. A Relying Party that obtains it obtains those three attributes as well, whether or not it requested them and whether or not it intends to use them.*

## RO_PID_51 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_51 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns requesting an identifier a Relying Party does not need.

*The CNP is a stable, lifetime-unique value, which is what makes it attractive as a database key and what makes it dangerous as one. Two Relying Parties that each hold it can join their records on it exactly, and neither needs the other's cooperation to do so. Since RO_PID_15 leaves the Romanian PID with no other persistent identifier, the ordinary pressure on a Relying Party is to request the CNP for purposes an opaque number would serve. RO_PID_50 and this provision exist to resist that pressure: the absence of a low-disclosure identifier is a reason to request no identifier, not a reason to request the high-disclosure one.*

*Taken together, these allow the pattern that most Relying Parties actually need: verify the User's identity once against the PID, bind a Pseudonym to that verification, and recognise the User by the Pseudonym thereafter — retaining no identifier from the PID at all. A Relying Party that adopts it satisfies RO_PID_50 and RO_PID_51 without giving up anything it needed.*

*This note is informative. Pseudonyms are a function of the Wallet Unit, governed by Topic 11 in Annex 2 of the ARF and by [CIR 2024/2979]; nothing in this Rulebook adds to or varies those requirements.*

*What a Relying Party does in the meantime.* Where a Pseudonym is not available to it, the alternatives RO_PID_51 names are the Relying Party's own — an account, a pseudonymous identifier of its own, or a prior authentication. A Relying Party that has none of those, and a lawful basis for the CNP, is not in breach of RO_PID_50 by requesting it. The provision does not depend on Topic 11 having shipped; the pattern described above becomes available when it does.

*The alternative that RO_PID_51 assumes.* Topic 11 in Annex 2 of the ARF requires every Wallet Unit to enable a User to generate a Pseudonym and register it at a Relying Party (PA_01), and to authenticate with that Pseudonym on subsequent visits to the same Relying Party (PA_02). Two of its properties make a Pseudonym the mechanism a Relying Party should reach for in place of the CNP:

- A Wallet Unit does not reveal the same Pseudonym to different Relying Parties, unless the User explicitly chooses otherwise (PA_16). Absent such a choice, Pseudonyms held by different Relying Parties therefore cannot be joined, whereas the CNP held by each of them can be, exactly and without their cooperation — and without the User's knowledge, let alone their choice.

- Where a Pseudonym is registered in the course of a presentation of a PID to the same Relying Party, that Relying Party can verify that the same User performed both actions (PA_12).

## RO_PID_52 — reasoning retained for a reserved provision (Annex D, N12)

> **Not settled.** RO_PID_52 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns retention of the portrait by a Relying Party.

*This provision transposes requirement PID_03a in Topic 3 in Annex 2 of the ARF. It is the only provision of this Rulebook that governs what a Relying Party does with an attribute after obtaining it, rather than whether it may request it. It is placed here because both questions are settled at the point of a presentation request, and because a Relying Party reading only the restrictions on requesting would otherwise never encounter it.*

## RO_PID_53 — Romania SHALL notify DGEP as a PID Provider to the Commission as specified in the European Digital…

*Rows 3 and 4 of the notification table are the two most easily overlooked.* The trust anchor that authenticates a status list is not the trust anchor that signs a PID, and RO_PID_54 governs only the latter; a status list that a Relying Party cannot authenticate is a status list it cannot act on. Requirements PPNot_03, PPNot_03a and PPNot_04 are what impose the three assurances the provision states.

*Row 4 matters beyond notification.* The private key of that access certificate is what will sign the Credential Issuer Metadata under the issuance protocol RO_PID_33 will settle, so a Wallet Unit that cannot authenticate the certificate will not be able to rely on the metadata either.

*Notification and registration are separate obligations with separate consequences, and are easily conflated. Notification under Topic 31 is what puts DGEP's trust anchors where a Relying Party can find them, and is what the rest of this chapter governs. Registration under Topic 27 is what makes DGEP a recognised PID Provider in the first place, and it is what causes a registration certificate to be issued to it under RPRC_13 — the certificate that RO_PID_33, once settled, will require DGEP to publish in its Credential Issuer Metadata, and whose contents RPRC_15 requires to state the attestation types registered here. The two duties in the final paragraph of the provision are requirements Reg_10e and Reg_08, which bind a PID Provider directly; the vetting is the Member State's under Reg_19, which requires it to approve a PID Provider against a defined policy before entering it in the registry, and under Reg_20, which requires it to identify PID Providers at a level of confidence proportionate to the risk. Both are outside this Rulebook.*

*On the list a Relying Party actually goes to.* [PID Rulebook] Section 6 says the Commission publishes the trust anchors of notified PID Providers in a **Trusted List**, and [PID Rulebook] prevails over the ARF where the two disagree, which would point a Relying Party at a Trusted List. The disagreement is resolved by fact rather than by drafting: the Commission publishes the list of PID Providers as a **List of Trusted Entities** under [ETSI TS 119 602], which is what PPNot_05 and PPNot_07 in Annex 2 of the ARF require and what the published list is. A Rulebook that directed Relying Parties to a Trusted List would direct them to something that does not hold DGEP's trust anchors, and Romanian PIDs would be unverifiable by any Relying Party that followed it. Chapter 6 therefore follows the ARF on this point and not [PID Rulebook].

## RO_PID_54 — The private keys used by DGEP to sign Romanian PIDs SHALL be generated and held in a hardware security…

*The certification levels above are stated as a minimum. This Rulebook specifies the assurance level required and not a product; replacing a module with any other meeting these levels does not require an amendment to this Rulebook.*

*Why DGEP operates the infrastructure, and why it matters.* The alternative — DGCTI operating the signing service on behalf of DGEP — creates a problem no drafting can solve. DGCTI is the Wallet Provider of RO Wallet, and **WIAM_12a** in Topic 40 in Annex 2 of the ARF forbids a Wallet Provider to learn which attestations a Wallet Instance holds. The signing service of the sole PID Provider sees every issuance and every replenishment, so placing it with the Wallet Provider would route to that Wallet Provider precisely the knowledge WIAM_12a denies it, by a path the requirement does not contemplate and no drafting can close. **DGEP operating its own signing infrastructure removes the position rather than mitigating it**, which is the only clean answer, and it also puts the keys that sign a PID in the hands of the authority accountable for the PID.

## RO_PID_55 — DGEP, RO Wallet and Relying Parties SHALL use only cryptographic algorithms included in the agreed list.

*Why the provision does more than transpose OIA_03 and WUA_04.* Those two requirements constrain the set an algorithm may be drawn from and select nothing from it. That is the right shape for a requirement addressed to the whole ecosystem, and the wrong shape for a national Rulebook whose stated purpose, in Section 1.1, is that a party implementing or verifying a Romanian PID need not consult anything else. A Relying Party in another Member State that receives a Romanian PID has to verify a signature, and it cannot do that from a permitted set; it needs to know which algorithm was used. Two implementations that each conform to a permitted-set constraint and choose differently do not interoperate, and neither has departed from the text. Naming a mandatory-to-implement set is what removes that outcome.

*Who publishes the profile.* The technical profile is DGEP's. A profile fixes what DGEP issues, so it is published in the name of the party bound by it — and since DGEP also operates the signing infrastructure under RO_PID_54, the party that publishes the profile is the party whose keys apply it.

*Why ECDSA with P-256 and SHA-256.* It is the algorithm the surrounding specifications assume: it is COSE algorithm `-7`, the default of the [ISO/IEC 18013-5] and [SD-JWT VC] ecosystems, supported by every Wallet Secure Cryptographic Device the Romanian PID is expected to be issued into, and present in the [ECCG Agreed Cryptographic Mechanisms]. Choosing anything stronger would exclude hardware without adding assurance the rest of the design relies on; choosing anything else would be a departure from what implementers already build.

*Why the set is a floor and not a closed list.* Curve and hash agility is the one property a document of this longevity cannot do without — the Rulebook outlives by many years the four-year administrative validity period of any PID issued under it — and an amendment to this Rulebook is a slower instrument than a published profile. The third paragraph therefore lets DGEP add algorithms without an amendment, subject to two constraints that between them prevent the discretion from undoing the provision: anything added must itself be in the [ECCG Agreed Cryptographic Mechanisms], and nothing required here may be withdrawn while a technical PID using it is still valid. A profile that could remove an algorithm in current use would strand attestations already in circulation.

*The table is a national election and is what makes this Rulebook implementable. A Relying Party in another Member State encountering a Romanian PID has to verify a signature, and a party building against this Rulebook has to choose an algorithm; a constraint that names only a permitted set leaves both of them to guess, and two conforming implementations that guess differently do not interoperate. Naming a mandatory-to-implement set removes that failure without closing the door on others, which is what the third paragraph preserves.*

*The [ECCG Agreed Cryptographic Mechanisms] is maintained outside this Rulebook and is revised. It is one of the instruments RO_PID_61 requires this Rulebook to be reviewed against, and a revision that withdrew any algorithm named above would require this provision to be amended.*

## RO_PID_56 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_56 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns publication of revocation status.

*The two encodings do not share a revocation mechanism, and an implementation that publishes only one is not conformant for the other. VCR_11 governs [ISO/IEC 18013-5]-compliant PIDs and routes them to the CBOR mechanism carried in Annex 2 of [CIR 2024/2979], the text of which is taken from the forthcoming second edition of [ISO/IEC 18013-5]. VCR_11a governs [SD-JWT VC]-compliant PIDs and routes them to [Token Status List]. Because RO_PID_03 requires every logical Romanian PID to be issued in both formats, DGEP operates two status list services and not one.*

*Why an Attestation Status List and not an Attestation Revocation List.* VCR_01 permits either for the [ISO/IEC 18013-5] encoding, and requirement ARB_23 in Topic 12 obliges this Rulebook to state which. An Attestation Revocation List enumerates the identifiers of revoked attestations, which requires each technical PID to carry a distinct identifier that is disclosed on presentation — a correlator of exactly the kind RO_PID_15 and RO_PID_39 exist to deny. An Attestation Status List carries an index into a bitstring instead, which discloses nothing beyond the index itself. VCR_11a also makes an Attestation Status List the only option for the [SD-JWT VC] encoding, so choosing it for both keeps the two encodings aligned.

*The technical validity period in RO_PID_38 does not make revocation unnecessary. VCR_01 and VCR_01b excuse a PID Provider from operating a revocation mechanism only where every attestation it issues is valid for 24 hours or less, which is not the case here.*

## RO_PID_57 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_57 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the operation of the status lists.

*The first is the most consequential.* RO_PID_15 declines to issue `document_number` on the ground that a constant value presented alongside rotating technical PIDs would defeat the rotation. A status-list index is exactly such a value — it is carried in the technical PID, it is disclosed to every Relying Party that receives it, and if indices were assigned sequentially as PIDs were issued then two indices from one batch would be adjacent, and adjacency would identify the User as surely as a document number. Randomising the index is what prevents the revocation mechanism from reintroducing, in Chapter 7, precisely the correlator Chapter 2 refuses to create.

*The second protects the User against DGEP rather than against a Relying Party.* If a list were small enough, DGEP could infer from a request for it which PID had probably just been presented, and to whom. That is a form of issuer-side tracking that the Regulation does not permit and that the User has no means of detecting.

*The third protects against both.* Requiring authentication to download a list would give DGEP a record of which Relying Parties check which lists and when — again, a picture of where Users are transacting, assembled by the party least able to justify holding it.

*These transpose requirements VCR_17, VCR_18 and VCR_16 in Topic 7 in Annex 2 of the ARF, and each of them closes a way in which the revocation mechanism could undo what the rest of this Rulebook does.*

## RO_PID_58 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_58 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the cascade from a revoked logical PID.

*Revoking only the logical PID would leave outstanding technical PIDs valid for up to two months after the ground for revocation arose, which for grounds such as the death of the User or the compromise of a Wallet Unit is the period during which revocation matters most. The technical validity period places no useful bound on that exposure. The cascade is the only mechanism that removes an outstanding technical PID from circulation.*

*The prohibition is requirement VCR_04 in Topic 7 in Annex 2 of the ARF. A revocation that can be reversed is not a revocation: a Relying Party that has cached a status list, as RO_PID_59 and requirement VCR_15 both contemplate, would continue to treat a reinstated PID as revoked until its cache expired, so reversal produces a period in which the same PID is valid for some Relying Parties and revoked for others.*

## RO_PID_59 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_59 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns revocation checking by Relying Parties.

*Republishing on a fixed schedule regardless of change keeps the publication interval from disclosing whether a revocation has occurred, and gives Relying Parties a predictable freshness bound.*

*Why 24 hours here and two months in RO_PID_38.* The two intervals answer different questions and are not to be aligned with one another. This provision bounds how far out of date a Relying Party's view of revocation status may be, and it is the only provision that bounds it. Setting it in step with the technical validity period would mean a revoked Romanian PID could be accepted for up to two months after its revocation.

*On the strengthening of VCR_13, and on the case it does not cover.* Requirement VCR_13 in Topic 7 in Annex 2 of the ARF states revocation checking as a SHOULD, and requires a Relying Party that departs from it to perform a risk analysis first. This provision makes checking a SHALL, which is a deliberate national strengthening of a choice the ARF leaves open, and it is permitted because it forbids nothing the ARF requires.

*It does not follow that revocation information is always available.* Requirement VCR_14 obliges a Relying Party to reach a reasoned decision where it is not, and the paragraph above transposes it. The case is not hypothetical for the Romanian PID: an [ISO/IEC 18013-5]-compliant presentation takes place over a proximity link, and a Relying Party Instance operating without connectivity holds only what it has cached. That is exactly the situation in which a fresh status list cannot be obtained and the cached one may have aged past 24 hours. The final sentence, which reflects requirement VCR_15, is what makes such a cache available in the first place; a Relying Party that fetches a list only when a User presents a PID both fails offline and discloses to DGEP when it is transacting.

## RO_PID_60 — reasoning retained for a reserved provision (Annex D, N13)

> **Not settled.** RO_PID_60 carries no content in version 0.1 of the Rulebook and its identifier is reserved. Nothing below is a requirement, and it concerns the grounds on which DGEP revokes.

*Why the Wallet Instance and device ground is drafted as a duty and not only as a ground.* Every other ground in the table is an event that reaches DGEP: a death or a change of citizenship is recorded in RNEP, a lost Wallet Unit is reported, a User asks. This one is not. The revocation of a Wallet Instance or of a Wallet Secure Cryptographic Device happens at the Wallet Provider, and nothing carries it to DGEP; the revocation references in the Wallet Instance Attestation and the Key Attestation are the means by which DGEP can find out, and they only work if somebody looks. A ground that nobody is obliged to look for is not a control, which is why WURevocation_18 and WUA_29 are both drafted as a continuing verification duty rather than as a trigger, and why this provision follows them.

*Why 24 hours, when the ARF says only "regularly".* The figure is national and is derived from the rest of Chapter 7 rather than chosen freely. RO_PID_59 already republishes each status list every 24 hours and already requires a Relying Party to work from a list no older than that. Setting the verification interval to the same figure makes the whole path bounded by one number: a device is revoked, DGEP detects it within 24 hours, revokes immediately, the status list carrying that revocation is republished within 24 hours, and the Relying Party is working from a list within its own 24-hour window. A longer verification interval would place the delay at the head of that chain, where none of the later bounds can recover it — the status list cannot publish a revocation DGEP has not yet made. It also lets DGEP run one daily cycle rather than maintain two schedules, and it aligns with the 24-hour threshold that VCR_09 already sets and that RO_PID_43 already uses.

*Why the second limb costs nothing.* RO_PID_33 already requires both attestations to be verified, including their revocation status, before issuance. Applying that to every batch rather than only to the first is not new work; it is the removal of an unstated assumption that replenishment under RO_PID_42, which is automatic and requires no action by the User, is somehow a lesser event than first issuance. It is not: it puts fresh, presentable attestations into a device that may since have been revoked.

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

