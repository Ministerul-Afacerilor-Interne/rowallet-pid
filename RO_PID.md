# Romanian PID Rulebook

**National Rulebook for natural-person Person Identification Data issued in Romania**

Ministry of Internal Affairs — General Directorate for Persons' Records (DGEP), PID Provider<br>
Ministry of Internal Affairs — Directorate-General for Communications and Information Technology (DGCTI), Wallet Provider

**Author:** Ministerul Afacerilor Interne, Direcția Generală pentru Evidența Persoanelor<br>
**Previous authors:** none — this is the first edition of this Rulebook.<br>
**Feedback:** feedback.pidrulebook@mai.gov.ro

---

## Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | 31 Aug 2026 | Phase 1 Draft. |

**EU baseline.** This Rulebook profiles the PID Rulebook (ARF Annex 3.01) **version 1.7, dated 17 July 2026**, and version **1.5** of the template for Attestation Rulebooks, dated 8 July 2026. It was assessed against the revisions of Annex 2 of the ARF in force on **4 August 2026** for Topic 3, recorded in Annex B, and on **7 August 2026** for Topic 12, recorded in Annex C. RO_PID_61 governs the review of this Rulebook against later versions of those documents and of the Implementing Regulations it depends on, and requires the dates recorded here to be updated on completion of every review.

---

## 1 Introduction

### 1.1 Document scope and purpose

This document is the Romanian PID Rulebook. It specifies how natural-person Person Identification Data (PID) is composed, encoded, issued, presented, and revoked in Romania, within the national European Digital Identity Wallet ecosystem (RoEUDIW).

This Rulebook is a national profile of the PID Rulebook [PID Rulebook], which forms Annex 3.01 of the Architecture Reference Framework [ARF]. It restates the requirements of [PID Rulebook] that apply to Romanian PIDs, and adds the national provisions that [PID Rulebook] and Topic 3 in Annex 2 of the ARF leave to Member States. It is self-contained as to what it settles: for any matter this Rulebook decides, a party implementing, issuing, or verifying a Romanian PID does not need to consult [PID Rulebook] in parallel. Section 1.3 and Annex D record what it does not yet decide.

This Rulebook does not amend [PID Rulebook]. Where a provision of this Rulebook is inconsistent with [PID Rulebook], [CIR 2024/2977], or the European Digital Identity Regulation, those instruments prevail.

**Scope of this version.** This version of the Rulebook governs the issuance of Romanian PIDs to **Romanian citizens**. The issuance of a PID to a foreign national resident in Romania is out of scope of this version of this document, and no provision of this version of this Rulebook applies to such a PID.

Person identification data for the legal person is out of scope of this document.

The Romanian PID carries age assertions as domestic attributes, defined in Section 2.7 and governed by RO_PID_20.

The Romanian PID does not carry the address of the User. Section 2.3 records that decision and RO_PID_11 states it. Where an attestation of address is required, it is issued separately and is out of scope of this document.

### 1.2 Document structure

This Rulebook follows the chapter structure of [PID Rulebook]. National material is placed in terminal subsections so that the two documents can be read side by side.

| Chapter | Content |
|---|---|
| Chapter 1 | Scope, structure, key words, terminology, and the national context in which this Rulebook operates. |
| Chapter 2 | PID attributes and metadata at a generic level, independent of encoding, including the Romanian domestic attributes. |
| Chapter 3 | Encoding of the Romanian PID in accordance with [ISO/IEC 18013-5]. |
| Chapter 4 | Encoding of the Romanian PID in accordance with [SD-JWT VC]. |
| Chapter 5 | Issuance, lifecycle, presentation, and restrictions on requesting attributes. **Section 5.1, enrolment and issuance, is in force; Sections 5.2 to 5.4 are withdrawn pending decision — N12.** |
| Chapter 6 | Trust anchors used to verify Romanian PIDs, and, in Section 6.1, the cryptographic algorithms used. |
| Chapter 7 | Revocation of Romanian PIDs and revocation checking by Relying Parties. **Withdrawn pending decision — N13.** |
| Chapter 8 | Compliance of this Rulebook with the EUDI framework, the ARF, and the relevant Regulations, and, in Section 8.1, the obligation to maintain that compliance. |
| Chapter 9 | References. |
| Annex A | National decision register. **Withdrawn pending decision — N16.** |
| Annex B | Conformance with Topic 3 in Annex 2 of the ARF, recorded requirement by requirement. |
| Annex C | Conformance with Topic 12 in Annex 2 of the ARF and with the template for Attestation Rulebooks, recorded requirement by requirement. |
| Annex D | Register of the provisions of this Rulebook that are under review. |

**Companion documents.** Two documents accompany this Rulebook and form no part of it. Neither is normative, and where either differs from this Rulebook, this Rulebook governs.

| Document | Content |
|---|---|
| `Rationale.md` | The reasoning behind the national decisions taken here. |
| `RO_PID_Data_Model.md` | The data model of the Romanian PID, for implementers: the attributes and claims of Chapters 2 to 4 restated in one place, with worked examples of a complete attestation in each encoding. It also restates what an implementer needs from Chapter 1 and from Section 6.1. |

*Where a provision states which requirement of the ARF or of an Implementing Regulation it transposes, that statement is kept here rather than in `Rationale.md`, because the review obligation in RO_PID_61 depends on it.*

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

Normative provisions specific to Romania are identified as **RO_PID_nn**, numbered consecutively in the order in which the document reads. **While this Rulebook is a draft the numbering is closed up whenever a provision is removed**, so an identifier is not stable between draft versions and a cross-reference from outside this document should cite the version it was taken from. From the first published version onwards an identifier will be retired rather than reassigned.

A provision or section marked **UNDER REVIEW** is not settled. It SHALL be read subject to the entry recorded for it in Annex D, and SHALL NOT be treated as a final national decision. Every such marking carries an Annex D register number, and Annex D carries no entry without a marking in the text. Three forms are used.

- Where the marked text reads ***To be established — under analysis***, the content of the provision or section **is withdrawn**. Nothing is required or permitted by it, and it cannot be implemented against or assessed for conformance until it is settled.
- Where the marked text states a rule, that rule is the position of this Rulebook as currently drafted and may be implemented against, but it may change.
- Where the marked text withdraws **a particular value** inside a provision that otherwise remains in force, the provision applies and only that value is unsettled. RO_PID_17 is the case: the attribute `trust_anchor` SHALL be included and `attestation_legal_category` SHALL contain `PID`, while the URL that `trust_anchor` carries is *to be established*.

**The identifiers of a withdrawn provision are reserved within the current draft.** A cross-reference elsewhere in this Rulebook to a provision whose content is withdrawn is a reference to that provision **as it will be settled**, and is not a defect in the cross-reference. This applies to RO_PID_33 to RO_PID_52, and to RO_PID_56 to RO_PID_60, whose sections are withdrawn in full.

**This Rulebook cannot presently be notified or assessed as a whole.** Sections 5.2 to 5.4 and Chapter 7 carry no content, and Annexes B and C record which requirements are consequently not transposed. That is the intended state for the present round and not an oversight.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF. In addition, the following Romanian terms are used with the meanings given below.

| Term | Meaning |
|---|---|
| **MoIA** | The Ministry of Internal Affairs. |
| **RNEP** | *Registrul Național de Evidență a Persoanelor* — the National Register of Persons, the population register of Romania and the source of every attribute of a Romanian PID. |
| **CEI** | *Cartea electronică de identitate* — the Romanian electronic identity card, issued on the basis of RNEP. It is used for onboarding and is not a source of PID attribute values. |
| **CNP** | *Cod numeric personal* — the Romanian personal numeric code, a 13-digit unique identifier. |
| **RoEUDIW** | The Romanian national European Digital Identity Wallet ecosystem. |
| **RO Wallet** | The Wallet Solution provided by the Ministry of Internal Affairs through DGCTI. |

### 1.5 National context

#### 1.5.1 Legal basis

| Instrument | Subject |
|---|---|
| **[Reg. eIDAS 2]** | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014, establishing the European Digital Identity Framework and the European Digital Identity Wallet. |
| **[CIR 2015/1502]** | Commission Implementing Regulation (EU) 2015/1502 on minimum technical specifications and procedures for assurance levels for electronic identification means. The basis of the level of assurance required by RO_PID_02 and of the enrolment and activation requirements in Section 5.1. |
| **[CIR 2024/2977]** | Commission Implementing Regulation (EU) 2024/2977 on person identification data and electronic attestations of attributes. Source of the PID attributes and metadata. |
| **[CIR 2024/2979]** | Commission Implementing Regulation (EU) 2024/2979 on the core functionality of the European Digital Identity Wallet. |
| **[CIR 2024/2980]** | Commission Implementing Regulation (EU) 2024/2980 on the notification to the Commission of electronic identification schemes and of providers. |
| **[CIR 2024/2982]** | Commission Implementing Regulation (EU) 2024/2982 on protocols and interfaces for issuance and presentation. |
| **[CIR 2025/1569]** | Commission Implementing Regulation (EU) 2025/1569. Article 8 establishes the catalogue of schemes for the attestation of attributes, in which RO_PID_30 requires a registration for the Romanian PID to reference this Rulebook. |
| **[ARF]** and **[PID Rulebook]** | The Architecture Reference Framework and its Annex 3.01, the technical reference profiled by this Rulebook. |
| **[OUG 97/2005]** | *Ordonanța de urgență* no. 97/2005 on the records, domicile, residence and identity documents of Romanian citizens, republished as amended. Article 6 establishes the CNP, defines it as a number that uniquely individualises a natural person, and provides that it is generated by DGEP. |
| **[Law 119/1996]** | Law no. 119/1996 on civil status documents, republished as amended. Article 22(1), with Article 6(1) of [OUG 97/2005], provides that the CNP is assigned from birth. |

#### 1.5.2 Roles and responsibilities

| Entity | Role | Responsibility |
|---|---|---|
| **MoIA — DGEP**<br>*Direcția Generală pentru Evidența Persoanelor* | **PID Provider** | Issuance and revocation of the Romanian PID at level of assurance high; correctness and provenance of the attributes; the attribute policy; identity proofing at enrolment; publication of the Type Metadata for the domestic type and of this Rulebook in the catalogue of attestation rulebooks; preparation of the information notified under RO_PID_53, including the trust anchors. |
| **MoIA — DGCTI**<br>*Direcția Generală pentru Comunicații și Tehnologia Informației* | **Wallet Provider** | Provision and operation of RO Wallet and its supporting infrastructure; encoding, cryptography, and the public key infrastructure of the Wallet Solution; interoperability. |

**RO_PID_01** — DGEP SHALL be the sole PID Provider of the Romanian PID. No other entity SHALL issue an attestation using the domestic namespace `eu.europa.ec.eudi.pid.ro.1` or the Verifiable Credential Type `urn:eudi:pid:ro:1` defined in Chapters 3 and 4 of this Rulebook.

*The document type `eu.europa.ec.eudi.pid.1`, and the namespace of the same name, are not domestic identifiers. PID_04 and PID_05 in Topic 3 in Annex 2 of the ARF require every PID Provider in the Union to use them for an [ISO/IEC 18013-5]-compliant PID, which under PID_02 every PID Provider issues. Nothing in this Rulebook restricts their use.*

**This provision further provides that a Wallet Unit SHALL hold at most one logical Romanian PID.** Where a Wallet Unit already holds a valid logical Romanian PID, DGEP SHALL NOT issue a second one to it, and the Wallet Unit SHALL NOT request one. This does not limit the number of technical PIDs a Wallet Unit holds for that logical PID, which the batch rules in Sections 5.2 to 5.4 will govern.

*Whether one logical PID may be issued to two Wallet Units of the same User — the case of a User with a personal and a work device — is not addressed by this Rulebook. The rule above forbids two PIDs in one Wallet Unit and says nothing about one PID in two.*

**RO_PID_02** — The Romanian PID SHALL be issued at level of assurance high, as defined in the European Digital Identity Regulation and the applicable Implementing Acts.

**RO_PID_03** — DGEP SHALL issue every logical Romanian PID in both the format specified in [ISO/IEC 18013-5] and the format specified in [SD-JWT VC]. Every batch of technical PIDs issued to a Wallet Unit SHALL contain technical PIDs in both formats.

*Transposes requirement PID_02 in Topic 3 in Annex 2 of the ARF.*

#### 1.5.3 National source registries

**RO_PID_04** — RNEP SHALL be the authoritative source for every PID attribute derived from civil-status or population records. DGEP SHALL NOT populate such an attribute from any other register, and SHALL NOT populate an attribute with data asserted by the User.

**The CEI is not a source of attribute values.** It is used for onboarding, under RO_PID_31. Where a value held on a CEI differs from the value of record in RNEP, RNEP governs and the PID carries the RNEP value.

The attributes sourced from RNEP are the current names, the date and place of birth, the facial image and the CNP. Citizenship is not among them: RO_PID_08 fixes the value of `nationality` rather than copying it, and RO_PID_07 likewise composes `birth_place` from what RNEP records rather than reproducing a stored string. The age assertions in `age_equal_or_over` are derived from the date of birth of record in RNEP and are not separately held there.

---

## 2 PID attributes and metadata

### 2.1 Introduction

Sections 2.2 to 2.5 list the mandatory and optional PID attributes and PID metadata defined in [CIR 2024/2977]. Section 2.6 lists the additional optional attributes defined in [PID Rulebook]. Section 2.7 defines the Romanian domestic attributes, in accordance with requirement PID_06 in Topic 3 in Annex 2 of the ARF.

The data identifiers and definitions in Sections 2.2 to 2.6 are those of [CIR 2024/2977] and [PID Rulebook]. They are independent of any encoding. Consequently, the data identifiers in these tables are not necessarily the attribute identifiers used for [ISO/IEC 18013-5]-compliant PIDs, nor the claim names used for [SD-JWT VC]-compliant PIDs; those are specified in Chapters 3 and 4 respectively. Data types are likewise not specified in this chapter.

Each table carries a **National provision** column stating, for each attribute, whether it is issued in the Romanian PID and under what rule. The levels used are those of [RFC 2119]. The second column below states the presence category each level corresponds to for the purposes of requirement ARB_09 in Topic 12 in Annex 2 of the ARF, which requires the presence of every attribute to be stated as mandatory, optional, or conditional.

| Level | Presence under ARB_09 | Meaning in this Rulebook |
|---|---|---|
| **SHALL be included** | mandatory | DGEP issues the attribute in every Romanian PID, subject only to any User opt-out expressly provided for. |
| **SHALL be included where** ⟨condition⟩ | **conditional** | DGEP issues the attribute in every Romanian PID in which the stated condition holds, and in no other. The condition is objective and is determined by the record in RNEP, not by DGEP's discretion. |
| **SHOULD be included** | optional | DGEP issues the attribute wherever the underlying data exists in RNEP. |
| **MAY be included** | optional | DGEP issues the attribute at its discretion, under the stated condition. |
| **SHALL NOT be included** | not present | DGEP does not issue the attribute. The reason is stated. |

**Two members of one attribute have conditional presence.** Of `birth_place`, the `country` member is present in every Romanian PID; `region` is present where RNEP records a county for the place of birth, and `locality` where RNEP records anything below the country. RO_PID_07 governs both. No attribute of the Romanian PID is conditional as a whole; every one of them is issued in every Romanian PID.

Inclusion of an attribute in the Romanian PID does not oblige a Relying Party to request it, nor a User to present it. A Relying Party is not required to request all mandatory attributes, and a User is allowed to refuse to present a mandatory attribute that is requested.

**RO_PID_05** — A string value in a Romanian PID that is **taken from RNEP** SHALL be carried exactly as recorded there, encoded in UTF-8. DGEP SHALL NOT change the case of such a value, SHALL NOT fold it to ASCII, SHALL NOT transliterate it, and SHALL NOT remove or substitute any character of it. This applies in both encodings specified in this Rulebook.

**RNEP records the family name and the given names in upper case**, with hyphens and with Romanian diacritics, and a Romanian PID carries them in that form.

**A value this Rulebook fixes is not taken from RNEP and is unaffected by the paragraph above.** RO_PID_12 fixes `issuing_authority` as a mixed-case string and `issuing_country` as `RO`; RO_PID_17 fixes `attestation_legal_category` as `PID`; RO_PID_08 fixes `nationality` as `RO`; and RO_PID_07 fixes the composition of `birth_place`, expanding the county to its full name and assembling the remainder.

A Relying Party SHALL NOT refuse a Romanian PID on the ground of the case or the diacritics of a string value. Where it compares such a value against a record of its own, it SHOULD normalise both sides by a documented rule rather than require a byte-for-byte match.

*The letters `Ă`, `Â`, `Î`, `Ș` and `Ț` occur in Romanian names and are carried as themselves. A value taken from a Romanian PID will therefore not match, byte for byte, the same value read from the machine-readable zone of the User's identity card, which [ICAO 9303] restricts to `A` to `Z`, `0` to `9` and `<`. The two differ in their diacritics and not in their case: the PID carries `IONEȘTEANU` where the machine-readable zone carries `IONESTEANU`.*

### 2.2 Mandatory attributes specified in CIR 2024/2977

| Data Identifier | Definition | National provision |
|---|---|---|
| **family_name** | Current last name(s) or surname(s) of the user to whom the person identification data relates. | **SHALL be included.** The current surname of record in RNEP, reproduced exactly, including Romanian diacritics. Example: `POPESCU-IONEȘTEANU` |
| **given_name** | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates. | **SHALL be included.** The current given name of record in RNEP, reproduced exactly, including Romanian diacritics. RNEP holds all given names of a User in a single field and this Rulebook does not decompose it. Examples: `IOAN-ANDREI`, `MARIA ECATERINA` |
| **birth_date** | Day, month, and year on which the user to whom the person identification data relates was born. If (partially) unknown, appropriate values complying with date formats in [ISO/IEC 18013-5] or [SD-JWT VC], as appropriate. | **SHALL be included.** See RO_PID_06. Example: `1978-02-12` |
| **birth_place** | The country as an alpha-2 country code as specified in [ISO 3166-1], or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. | **SHALL be included.** See RO_PID_07. Example: country `RO`, region `Cluj`, locality `Mun.Cluj-Napoca` |
| **nationality** | One or more alpha-2 country codes as specified in [ISO 3166-1], representing the nationality of the user to whom the person identification data relates. If unknown, value `QU`. If the user does not hold a nationality, value `QS`. | **SHALL be included.** See RO_PID_08. Example: `["RO"]` |
| **portrait** | Except where the user explicitly opts out, where applicable, the facial image of the user to whom the person identification data relates, compliant with the quality requirements for a full frontal image type as set out in [ISO/IEC 39794-5] or, for backward compatibility, [ISO/IEC 19794-5], clauses 8.2, 8.3 and 8.4, provided as encoded image data without the headers or blocks as specified in clause 5 of [ISO/IEC 19794-5], except for the image data itself (a JPEG). In case the user opts out, empty, as specified in PID_03 in Topic 3 in Annex 2 of the ARF. | **SHALL be included**, subject to the User opt-out and to the transitional rule in RO_PID_24. The facial image of record in RNEP — the same image from which the CEI is produced. See RO_PID_24, which governs the attribute. **UNDER REVIEW — N6.** |

*RNEP holds all of a User's given names in one field, and this Rulebook reproduces that field as it stands. It defines no rule for separating, ordering or normalising the names within it, and DGEP SHALL NOT remove a hyphen or any other character occurring in the recorded value.*

**RO_PID_06** — `birth_date` SHALL be taken from the date of birth of record in RNEP. It SHALL NOT be derived from the CNP.

**RO_PID_07** — `birth_place` SHALL be derived from the place of birth of record in RNEP and composed as this provision requires. It carries the country as an alpha-2 country code as specified in [ISO 3166-1], or the state, and, if known, the **county** and the **territorial administrative unit** (*unitate administrativ-teritorială*, UAT) in which the User was born. A UAT can be a municipality (*municipiu*), a city (*oraș*) or a commune (*comună*). `birth_place` MAY additionally carry, besides the UAT, the locality (*localitate*) and the village (*sat*). For a Romanian citizen born outside Romania, `birth_place` carries the name of the country and, if known, the area of the place of birth.

For a User born in Romania the value is composed on the following template:

```
RO, Jud.JJ Mun./Orș./Loc./Sat./Com.Denumire [(Mun./Orș./Com.Denumire)]*
```

`*` The parenthesised element is used where the User was not born in a UAT, and names the UAT to which the place of birth belongs:

| Example |
|---|
| `Jud.CT Sat.Darabani (Orș.Negru Vodă)` |
| `Jud.MM Sat.Bârsana (Com.Bârsana)` |
| `Jud.CV Sat.Lunga (Mun.Târgu Secuiesc)` |
| `Jud.MM Loc.Iapa (Mun.Sighetu Marmației)` |

The value is distributed across the three members that both encodings define for this attribute as follows.

| Member | Carries |
|---|---|
| `country` | The [ISO 3166-1] alpha-2 code of the country of birth. `RO` for a User born in Romania. RNEP does not hold the country of birth as an alpha-2 code, and DGEP derives the code from the country of record. |
| `region` | **The county, written in full** — `Constanța`, not `CT`; `Maramureș`, not `MM`. Omitted where RNEP records no county. |
| `locality` | The remainder of the composed value: the territorial administrative unit and, where the User was not born in one, the *localitate* or *sat* with its UAT in parentheses. Where RNEP records no county, it carries the whole of the recorded place of birth apart from the country. |

Applying that to the examples above, a User born at *Darabani* carries `country` `RO`, `region` `Constanța` and `locality` `Sat.Darabani (Orș.Negru Vodă)`.

**Where no county is recorded.** Where RNEP records no county for the place of birth — in particular where the User was born outside Romania — `region` SHALL be omitted, and the whole of the recorded place of birth apart from the country SHALL be carried in `locality`. `country` is present in every case, so the requirement of Section 3.1.4 that at least one member be present is always met.

*Deriving the alpha-2 code from the country of record maps a recorded value onto the code set [CIR 2024/2977] requires. It is not the use of a second register, and RO_PID_04 is unaffected.*

`birth_place` is carried in the form this provision fixes and is not subject to the case rule in RO_PID_05.

*The county is carried in `region` and not inside `locality` because [PID Rulebook] defines `region` as "the name of a state, province, district, or local area" — a name, so the county written in full is what the member is for, and a code would be the departure. Carrying it in its own member also allows a Relying Party to request the county of birth without the locality, which RO_PID_26 makes possible in a [SD-JWT VC] presentation.*

**RO_PID_08** — The `nationality` attribute of a Romanian PID SHALL contain exactly one country code, and that code SHALL be `RO`.

*The attribute is the citizenship, rendered `cetățenie` in the official Romanian text of [CIR 2024/2977], and RNEP records Romanian citizenship. DGEP is not an authoritative source for a nationality conferred by another State, and this Rulebook defines no domestic attribute for one. The value is fixed by this provision rather than copied from the register, so the form in which RNEP holds citizenship does not bear on the attribute.*

### 2.3 Optional attributes specified in CIR 2024/2977

| Data Identifier | Definition | National provision |
|---|---|---|
| **resident_address** | The full address of the place where the user to whom the person identification data relates currently resides or can be contacted (street name, house number, city etc.). | **SHALL NOT be included.** See RO_PID_11. |
| **resident_country** | The country where the user to whom the person identification data relates currently resides, as an alpha-2 country code as specified in [ISO 3166-1]. | **SHALL NOT be included.** See RO_PID_11. |
| **resident_state** | The state, province, district, or local area where the user to whom the person identification data relates currently resides. | **SHALL NOT be included.** See RO_PID_11. |
| **resident_city** | The municipality, city, town, or village where the user to whom the person identification data relates currently resides. | **SHALL NOT be included.** See RO_PID_11. |
| **resident_postal_code** | The postal code of the place where the user to whom the person identification data relates currently resides. | **SHALL NOT be included.** See RO_PID_11. |
| **resident_street** | The name of the street where the user to whom the person identification data relates currently resides, including the house number and any affix or suffix thereof. | **SHALL NOT be included.** See RO_PID_11. |
| **resident_house_number** | The house number of the place where the user to whom the person identification data relates currently resides, including any affix or suffix thereof. *This data identifier is defined in [PID Rulebook] only as a member of the `address` claim, and is listed here so that this table is complete against the optional attributes a Romanian PID could have carried.* | **SHALL NOT be included.** See RO_PID_11. |
| **family_name_birth** | Last name(s) or surname(s) of the User to whom the person identification data relates at the time of birth. | **SHALL NOT be included.** See RO_PID_11. |
| **given_name_birth** | First name(s), including middle name(s), of the User to whom the person identification data relates at the time of birth. | **SHALL NOT be included.** See RO_PID_11. |
| **sex** | Values shall be one of the following: 0 = not known; 1 = male; 2 = female; 3 = other; 4 = inter; 5 = diverse; 6 = open; 9 = not applicable. For values 0, 1, 2 and 9, [ISO/IEC 5218] applies. | **SHALL NOT be included.** See RO_PID_11. |
| **personal_administrative_number** | A value assigned to the user to whom the person identification data relates that is unique among all personal administrative numbers issued by the provider of person identification data. Where Member States opt to include this attribute, they shall describe in their electronic identification schemes under which the person identification data is issued, the policy that they apply to the values of this attribute, including, where applicable, specific conditions for the processing of this value. | **SHALL NOT be included.** See RO_PID_10. |
| **email_address** | Electronic mail address of the user to whom the person identification data relates, in conformance with [RFC 5322]. | **SHALL NOT be included.** See RO_PID_09. |
| **mobile_phone_number** | Mobile telephone number of the User to whom the person identification data relates, starting with the '+' symbol as the international code prefix and the country code, followed by numbers only. | **SHALL NOT be included.** See RO_PID_09. |

**RO_PID_09** — `email_address` and `mobile_phone_number` SHALL NOT be included in the Romanian PID.

**RO_PID_10** — `personal_administrative_number` SHALL NOT be included in the Romanian PID.

**RO_PID_11** — The `resident_address`, `resident_country`, `resident_state`, `resident_city`, `resident_postal_code`, `resident_street` and `resident_house_number` attributes, and the `family_name_birth`, `given_name_birth` and `sex` attributes, SHALL NOT be included in the Romanian PID.

Together with RO_PID_09 and RO_PID_10, this provision has the effect that **the Romanian PID carries no optional attribute of [CIR 2024/2977] at all.** Every attribute it carries is either mandatory under [CIR 2024/2977], mandatory metadata, optional metadata that Section 2.5 makes mandatory here, one of the two additional attributes of [PID Rulebook] that Section 2.6 makes mandatory, or a domestic attribute defined in Section 2.7.

### 2.4 Mandatory metadata specified in CIR 2024/2977

| Data Identifier | Definition | National provision |
|---|---|---|
| **issuing_authority** | Name of the administrative authority that issued the person identification data, or the [ISO 3166-1] alpha-2 country code of the respective Member State if there is no separate authority entitled to issue person identification data. | **SHALL be included.** Fixed value; see RO_PID_12. |
| **issuing_country** | Alpha-2 country code, as specified in [ISO 3166-1], of the country or territory of the provider of the person identification data. | **SHALL be included.** Fixed value `RO`. |

**RO_PID_12** — `issuing_authority` SHALL contain the exact string `Direcția Generală pentru Evidența Persoanelor`, encoded in UTF-8 with Romanian diacritics. `issuing_country` SHALL contain the exact string `RO`.

The value of `issuing_authority` SHALL be carried in Romanian only. It SHALL NOT be translated, transliterated, abbreviated, or accompanied by a rendering in any other language, in either encoding specified in this Rulebook.

A translated form of the authority name is carried by the Credential Issuer Metadata DGEP publishes, by the Type Metadata published under RO_PID_29, and by the List of Trusted Entities of PID Providers compiled from the notification made under [CIR 2024/2980], each of which accommodates more than one language. A Wallet Unit or Relying Party SHOULD render `issuing_authority` in the language of its interface using those mechanisms, and SHALL transmit the Romanian value unchanged.

### 2.5 Optional metadata specified in CIR 2024/2977

| Data Identifier | Definition | National provision |
|---|---|---|
| **expiry_date** | Date (and if possible time) when the administrative validity period of the person identification data will expire. This attribute, as well as `issuance_date`, pertains to the administrative validity period of the logical PID, which is in general different from — and considerably longer than — the technical validity period of a technical PID. | **SHALL be included.** See RO_PID_13. |
| **issuance_date** | Date (and if possible time) when the person identification data was issued and/or the administrative validity period of the person identification data began. | **SHALL be included.** The date on which the logical PID was issued, in `YYYY-MM-DD` form. |
| **document_number** | A number for the person identification data, assigned by the provider of person identification data. | **SHALL NOT be included.** See RO_PID_15. |
| **issuing_jurisdiction** | Country subdivision code of the jurisdiction that issued the person identification data, as specified in [ISO 3166-2], Clause 8. The first part of the code shall be the same as the value for the issuing country. | **SHALL NOT be included.** See RO_PID_16. |

*The words "and if possible time" in the two definitions above are those of [CIR 2024/2977], which permits a time element to be carried. This Rulebook does not exercise that permission: RO_PID_14 requires both values to carry a date alone, and the encodings specified in Chapters 3 and 4 admit no time element in either.*

**RO_PID_13** — `expiry_date` SHALL be computed from `issuance_date`. It SHALL be set to the date **one day before the fourth anniversary** of `issuance_date`, so that the administrative validity period of a logical Romanian PID is exactly four years under the convention in RO_PID_14. Where `issuance_date` is 29 February, the anniversary is taken as 28 February.

*Example: a logical PID with `issuance_date` `2026-09-01` has `expiry_date` `2030-08-31`.*

`expiry_date` SHALL NOT be derived from the expiry date of the CEI on the basis of which the logical PID was issued, and the administrative validity period of a logical Romanian PID is independent of the validity of that document.

*[PID Rulebook] leaves it to the PID Provider to decide whether a logical PID has an administrative validity period at all, and how it is determined. Requirements PID_13 and PID_20 in Topic 3 in Annex 2 of the ARF require only that the PID Provider have a policy relating these dates to the technical validity period; RO_PID_14 is that policy.*

**RO_PID_14** — The relationship between the administrative dates and the technical validity period of a technical PID SHALL be as follows.

- `issuance_date` and `expiry_date`, and their [SD-JWT VC] counterparts `date_of_issuance` and `date_of_expiry`, carry no time element. For the purpose of relating them to technical validity, the administrative validity period of a logical PID begins at 00:00:00 on `issuance_date` and ends at 23:59:59 on `expiry_date`, both in the local time of Romania, converted to UTC wherever a technical field requires an instant.
- A Relying Party determining whether a Romanian PID is within its administrative validity period SHALL apply the convention in the preceding bullet, and SHALL NOT evaluate the two dates against its own local date. The two can differ by a day where the Relying Party is in another time zone. No such question arises for `validFrom`, `validUntil`, `nbf` and `exp`, which carry absolute instants.
- A technical PID SHALL NOT carry a `validFrom` or `nbf` earlier than the beginning, nor a `validUntil` or `exp` later than the end, of that administrative validity period. The technical validity period is always contained within the administrative validity period.
- DGEP SHALL cease supplying further technical PIDs when the administrative validity period ends.
- Throughout the administrative validity period, **DGEP SHALL keep available to the Wallet Unit a technical PID whose technical validity period has not expired**, and DGCTI SHALL ensure that RO Wallet requests one, under the replenishment rules to be settled in Sections 5.2 to 5.4. Neither duty discharges the other: DGEP cannot deliver a technical PID that is not requested, and a Wallet Unit cannot obtain one that is not offered.
- This policy SHALL be applied identically to both encodings, so that the administrative dates of the two formats of the same logical PID never diverge.

> **UNDER REVIEW — N8.** The division of this duty is to be confirmed.

*Transposes requirements PID_13 and PID_20 in Topic 3 in Annex 2 of the ARF, each of which requires the PID Provider to have such a policy.*

**RO_PID_15** — `document_number` SHALL NOT be included in the Romanian PID.

**RO_PID_16** — `issuing_jurisdiction` SHALL NOT be included in the Romanian PID.

### 2.6 Additional optional attributes specified in the EU PID Rulebook

| Data Identifier | Definition | National provision |
|---|---|---|
| **trust_anchor** | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the PID can be found or looked up. | **SHALL be included.** The value is *to be established — under analysis*; see RO_PID_17. **UNDER REVIEW — N9.** |
| **attestation_legal_category** | This attribute indicates that a PID has indeed been issued as a PID. | **SHALL be included.** Fixed value `PID`. |

**RO_PID_17** — `attestation_legal_category` SHALL contain the exact string `PID`. The value of `trust_anchor` is *to be established — under analysis*.

> **UNDER REVIEW — N9.** The value is not settled. It is embedded in every attestation issued and is to be fixed before first issuance.

The URL in `trust_anchor` is a convenience for Relying Parties and does not displace the List of Trusted Entities of PID Providers. Chapter 6 governs the authoritative provision of trust anchors.

### 2.7 Romanian domestic attributes

This section defines the domestic PID attributes of Romania, in accordance with requirement PID_06 in Topic 3 in Annex 2 of the ARF. Their encodings are specified in Sections 3.1.5 and 4.1.3.

**RO_PID_18** — The domestic attributes of the Romanian PID are exactly those listed in the table below. DGEP SHALL NOT issue any further domestic attribute in the Romanian PID without an amendment to this Rulebook.

| Data Identifier | Definition | National provision |
|---|---|---|
| **personal_numeric_code** | The *cod numeric personal* (CNP) assigned to the User under Romanian law. | **SHALL be included.** See RO_PID_19 and the restrictions on requesting it, to be settled in Section 5.4. Example: `1780212123451` |
| **age_equal_or_over** | A set of assertions, one for each age threshold defined in RO_PID_20, stating whether the User has attained that age. | **SHALL be included.** See RO_PID_20. Thresholds 14, 16, 18 and 65 |

**RO_PID_19** — `personal_numeric_code` SHALL contain the CNP of record in RNEP: exactly thirteen decimal digits, without separators, spaces, or any prefix. The first digit SHALL be in the range 1 to 6.

*The CNP is established by Article 6 of [OUG 97/2005], which defines it as a significant number that uniquely individualises a natural person and provides that it is generated by DGEP. Article 6(1) of that instrument with Article 22(1) of [Law 119/1996] provides that it is assigned from birth.*

*The first digit encodes the sex and the century of birth of the User. The range 1 to 6 is the range RNEP assigns to Romanian citizens, and this Rulebook governs the issuance of Romanian PIDs to Romanian citizens. A Relying Party SHALL NOT reject a CNP on any other ground drawn from the structure of the value.*

*A Wallet Unit SHOULD make the consequence of disclosing `personal_numeric_code` evident to the User at the point of approval, rather than presenting it as one identifier among others.*

**RO_PID_20** — `age_equal_or_over` SHALL assert, for each of the age thresholds **14, 16, 18 and 65**, whether the User had attained that age at the timestamp in the `validFrom` element of the Mobile Security Object, for [ISO/IEC 18013-5]-compliant PIDs, and at the timestamp in the `nbf` claim, for [SD-JWT VC]-compliant PIDs. Each assertion SHALL be a boolean. All four SHALL be present in every Romanian PID, whether true or false.

DGEP SHALL NOT issue an assertion at any other threshold. Adding a threshold requires an amendment to this Rulebook.

Each assertion SHALL be individually selectively disclosable, in both encodings; Sections 3.1.5 and 4.1.3 specify how.

Each assertion SHALL be derived from the `birth_date` of record in RNEP. It SHALL NOT be derived from the CNP, for the reason given in RO_PID_06.

*A threshold is added or removed only by amendment to this Rulebook, and RO_PID_23, RO_PID_26, RO_PID_27, Sections 3.1.5 and 4.1.3, and the technical validity rule to be settled in Sections 5.2 to 5.4 all follow it when one is.*

---

## 3 ISO/IEC 18013-5-compliant encoding of the Romanian PID

This chapter specifies the encoding of the Romanian PID where it complies with [ISO/IEC 18013-5]. This encoding is used principally for proximity presentation.

*Requirement ARB_02 in Topic 12 in Annex 2 of the ARF obliges the author of an Attestation Rulebook to analyse whether a User must be able to present the attestation in proximity to the Relying Party without using the internet, and, if so, to require the [ISO/IEC 18013-5] format. That analysis has been carried out. A Romanian PID is presented predominantly face to face, in settings where the User, the Relying Party, or neither, has connectivity. Both encodings are accordingly mandatory under RO_PID_03.*

### 3.1 Encoding of PID attributes and metadata

#### 3.1.1 Document type and namespaces

**RO_PID_21** — An [ISO/IEC 18013-5]-compliant Romanian PID SHALL use the document type `eu.europa.ec.eudi.pid.1`, as required by PID_04 in Topic 3 in Annex 2 of the ARF. It SHALL carry two namespaces:

| Namespace | Content |
|---|---|
| `eu.europa.ec.eudi.pid.1` | The attributes and metadata specified in Sections 2.2 to 2.6. Required by PID_05. |
| `eu.europa.ec.eudi.pid.ro.1` | The Romanian domestic attributes specified in Section 2.7. Constructed as PID_06 requires. |

*PID_06 requires the domestic namespace identifier to be generated by appending the [ISO 3166-1] alpha-2 country code, separated by a period, to the namespace identifier of PID_05 with the version number excluded, optionally followed by a version number. For Romania that yields `eu.europa.ec.eudi.pid` + `.ro` + `.1`.*

**RO_PID_22** — Every domestic attribute SHALL be carried in the `eu.europa.ec.eudi.pid.ro.1` namespace. A domestic attribute SHALL NOT be carried in the `eu.europa.ec.eudi.pid.1` namespace, and the structures defined in that namespace SHALL NOT be extended with domestic members.

#### 3.1.2 Attributes overview

The table below specifies the encoding of the attributes and metadata of Sections 2.2 to 2.6 in the `eu.europa.ec.eudi.pid.1` namespace. The encoding column uses CDDL representation types as defined in [RFC 8610]. The following applies throughout:

- `tstr`, `uint`, `bstr`, `bool` and `tdate` are CDDL representation types defined in [RFC 8610].
- A `tstr` SHALL be encoded in UTF-8 as specified in [RFC 8949] and SHALL support the full Unicode range. Romanian diacritics SHALL be preserved and SHALL NOT be transliterated.
- Every attribute of type `tstr` SHALL have a maximum length of 150 characters.
- `full-date` is defined as `full-date = #6.1004(tstr)`, where tag 1004 is specified in [RFC 8943].
- In accordance with [RFC 8949] Section 3.4.1, a `tdate` attribute SHALL contain a date-time string as specified in [RFC 3339]. In accordance with [RFC 8943], a `full-date` attribute SHALL contain a full-date string as specified in [RFC 3339].
- In dates, fractions of seconds SHALL NOT be used, and a local offset from UTC SHALL NOT be used; the time-offset defined in [RFC 3339] SHALL be set to `Z`.
- Three of the four rules for canonical CBOR in [RFC 8949] Section 4.2 SHALL be implemented for all CBOR structures in a Romanian PID: integers (major types 0 and 1) SHALL be as small as possible; the expression of the length in a `bstr`, `tstr`, array or map SHALL be as short as possible; and indefinite-length items SHALL be made into definite-length items.
- A Romanian PID SHALL contain at most one attribute with the same attribute identifier, as required by PID_11 in Topic 3 in Annex 2 of the ARF. This applies within each namespace and across both namespaces together.

Whether each attribute is present is governed by Chapter 2 and is restated in the final column.

| Data Identifier | Attribute identifier | Encoding format | Inclusion |
|---|---|---|---|
| family_name | `family_name` | `tstr` | SHALL |
| given_name | `given_name` | `tstr` | SHALL |
| birth_date | `birth_date` | `full-date` | SHALL |
| birth_place | `place_of_birth` | `place_of_birth`, see Section 3.1.4 | SHALL |
| nationality | `nationality` | `nationalities`, see Section 3.1.3 | SHALL |
| portrait | `portrait` | `bstr`, see RO_PID_24 | SHALL |
| resident_address | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_country | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_state | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_city | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_postal_code | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_street | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_house_number | — | not encoded | SHALL NOT, per RO_PID_11 |
| family_name_birth | — | not encoded | SHALL NOT, per RO_PID_11 |
| given_name_birth | — | not encoded | SHALL NOT, per RO_PID_11 |
| sex | — | not encoded | SHALL NOT, per RO_PID_11 |
| personal_administrative_number | — | not encoded | SHALL NOT, per RO_PID_10 |
| email_address | — | not encoded | SHALL NOT, per RO_PID_09 |
| mobile_phone_number | — | not encoded | SHALL NOT, per RO_PID_09 |
| expiry_date | `expiry_date` | `full-date` | SHALL |
| issuance_date | `issuance_date` | `full-date` | SHALL |
| issuing_authority | `issuing_authority` | `tstr` | SHALL |
| issuing_country | `issuing_country` | `tstr` | SHALL |
| document_number | — | not encoded | SHALL NOT, per RO_PID_15 |
| issuing_jurisdiction | — | not encoded | SHALL NOT, per RO_PID_16 |
| trust_anchor | `trust_anchor` | `tstr` | SHALL |
| attestation_legal_category | `attestation_legal_category` | `tstr` | SHALL |

#### 3.1.3 Attribute nationality

The attribute `nationality` is encoded as a type `nationalities`, that is, an array of alpha-2 country codes as specified in [ISO 3166-1]. Using CDDL notation as specified in [RFC 8610], the encoding of this attribute is:

```cddl
nationalities = [+ CountryCode]

CountryCode = tstr ; Alpha-2 country code specified in [ISO 3166-1]
```

In an [ISO/IEC 18013-5]-compliant attestation the whole array is presented whenever the User approves presentation of the attribute; individual elements cannot be selectively disclosed. This differs from the [SD-JWT VC] encoding, where PID_21 requires each array entry to be individually selectively disclosable; see RO_PID_26. By RO_PID_08 the array of a Romanian PID contains exactly one element, so the difference has no practical effect: a User disclosing `nationality` discloses that they hold Romanian citizenship and nothing further.

#### 3.1.4 Attribute place_of_birth

The attribute `place_of_birth` is encoded as a type `place_of_birth`. Using CDDL notation as specified in [RFC 8610], the encoding of this attribute is:

```cddl
place_of_birth =
{
  ? "country": tstr  ; a single alpha-2 country code as specified in [ISO 3166-1]
  ? "region": tstr   ; the name of a state, province, district, or local area
  ? "locality": tstr ; the name of a municipality, city, town, or village
}
```

`place_of_birth` SHALL contain at least one of the key-value pairs `"country"`, `"region"`, or `"locality"`. Which of them a Romanian PID carries, and what each holds, is governed by **RO_PID_07**, which fixes the value, the template on which it is composed, and how that value is distributed across the three members above.

The whole map is presented whenever the User approves presentation of the attribute; its members cannot be selectively disclosed independently. This is a genuine limitation of the [ISO/IEC 18013-5] encoding and it has no counterpart in the [SD-JWT VC] encoding, where PID_21 requires `country`, `region` and `locality` to be individually selectively disclosable; see RO_PID_26. A User who wishes to disclose only the country of birth can therefore do so in a remote presentation but not in a proximity presentation, and a Wallet Unit SHOULD make that clear at the point of approval. **What else a User can disclose on its own in a remote presentation follows from the distribution RO_PID_07 fixes**: the county of birth is carried in `region` and can therefore be released without the locality, whereas the elements composed into `locality` cannot be separated from one another.

#### 3.1.5 Encoding of Romanian domestic attributes

The table below specifies the encoding of the domestic attributes of Section 2.7 in the `eu.europa.ec.eudi.pid.ro.1` namespace. The encoding rules stated in Section 3.1.2 apply to these attributes as well.

| Data Identifier | Attribute identifier | Encoding format | Inclusion |
|---|---|---|---|
| personal_numeric_code | `personal_numeric_code` | `tstr`, exactly 13 decimal digits | SHALL |
| age_equal_or_over | `age_over_14` | `bool` | SHALL, per RO_PID_20 |
| age_equal_or_over | `age_over_16` | `bool` | SHALL, per RO_PID_20 |
| age_equal_or_over | `age_over_18` | `bool` | SHALL, per RO_PID_20 |
| age_equal_or_over | `age_over_65` | `bool` | SHALL, per RO_PID_20 |

**RO_PID_23** — In an [ISO/IEC 18013-5]-compliant Romanian PID, the age assertions SHALL be encoded as the separate top-level attributes of the `eu.europa.ec.eudi.pid.ro.1` namespace listed above, one for each threshold, and not as a single structured attribute.

*The [SD-JWT VC] encoding in Section 4.1.3 carries the same assertions as the members of one `age_equal_or_over` object. The difference is one of structure only: in both encodings any one assertion can be disclosed without the others. Implementers are not to reconcile the two.*

*Where the encodings genuinely diverge is elsewhere, and Sections 3.1.3 and 3.1.4 record it. A Relying Party SHALL NOT assume that a request satisfiable in one encoding is satisfiable identically in the other.*

### 3.2 Portrait

**RO_PID_24** — The `portrait` attribute of a Romanian PID SHALL contain the facial image of record in RNEP — the image from which the CEI of the User is produced.

The image must comply with the quality requirements for a full frontal image type set out in [ISO/IEC 39794-5] and must be provided as JPEG image data without the headers or blocks specified in clause 5 of [ISO/IEC 19794-5], as [CIR 2024/2977] requires. **Those requirements bind DGEP through that Regulation and this Rulebook does not restate them.** The encoding of the attribute is specified in Section 3.1.2 for an [ISO/IEC 18013-5]-compliant PID and in Section 4.1.1 for a [SD-JWT VC]-compliant PID.

**Transitional rule.** Until DGEP announces otherwise, the `portrait` attribute SHALL be issued with the empty value prescribed by RO_PID_25 — an empty CBOR `bstr` in an [ISO/IEC 18013-5]-compliant PID and an empty JSON string in a [SD-JWT VC]-compliant PID. The attribute SHALL be present in every Romanian PID and SHALL be empty.

**A Wallet Unit SHALL make evident to the User that the Romanian PID contains a `portrait` attribute and that its value is empty.** The attribute is not to be concealed while the transitional rule applies.

**This provision is where the portrait is governed.** Any further national requirement for the attribute — the pixel dimensions, the inter-eye distance and the JPEG quality setting from which portraits are produced, any constraint on the encoded size, and the date from which the value is populated — SHALL be added here rather than elsewhere in this Rulebook, so that a party implementing the portrait has one provision to read.

> **UNDER REVIEW — N6.** [CIR 2024/2977] makes the portrait mandatory only from a future date. The national requirements for the attribute are to be added to this provision before its value is populated.

**RO_PID_25** — DGEP SHALL enable every User to opt out from receiving a `portrait` attribute. Where a User exercises that opt-out, DGEP SHALL include the `portrait` attribute in the Romanian PID as an empty CBOR `bstr` in an [ISO/IEC 18013-5]-compliant PID, and as an empty JSON string in a [SD-JWT VC]-compliant PID. The attribute SHALL be present and empty; it SHALL NOT be omitted. DGEP SHALL NOT withhold any other attribute on the ground that the User has opted out.

**When the election is made, and changing it.** The opt-out is exercised during the issuance of the logical Romanian PID, as PID_03 in Topic 3 in Annex 2 of the ARF provides. A User MAY afterwards ask DGEP to change that election, and DGEP SHALL provide a means of doing so. **A change does not require a new logical Romanian PID**: it takes effect on the technical PIDs issued after it, through the re-issuance process required by Topic 10 in Annex 2 of the ARF, and the administrative validity period of the logical PID — and with it `issuance_date` and `expiry_date` — is unaffected.

**What becomes of the technical PIDs already issued.** They are signed and SHALL NOT be altered. **While the transitional rule in RO_PID_24 applies, a change of election changes no value**: `portrait` is empty whichever election is in force, so no technical PID is superseded, none is revoked, and the two rules below do not bite. They govern from the date DGEP populates the attribute, when applying a changed election does change the value of an attribute of the logical PID; the consequences are then the same as for any other attribute change:

- RO Wallet SHALL cease to present the superseded technical PIDs and SHOULD delete them, as requirement ISSU_62 in Topic 10 in Annex 2 of the ARF requires.
- DGEP SHALL revoke each superseded technical PID **that remains valid for at least 24 hours**, as requirement VCR_09 in Topic 7 in Annex 2 of the ARF requires. A technical PID with less than 24 hours of its technical validity period remaining is not revoked; it expires. The revocation mechanism itself is Chapter 7's, and that chapter is not settled.

**The moment that matters is when DGEP applies the changed election, not when the User asks.** DGEP MAY apply it at the next replenishment of the Wallet Unit rather than immediately, in which case no technical PID is superseded before its time and nothing is revoked.

*The machinery this needs already exists and is mandatory. Requirement ISSU_63 in Topic 10 in Annex 2 of the ARF obliges DGEP and RO Wallet to support the [OpenID4VCI] features enabling re-issuance, and ISSU_64 those enabling batch issuance; ISSU_58 obliges RO Wallet to give the User a means of initiating re-issuance; and ISSU_65 obliges DGEP to verify that a re-issued technical PID goes to the Wallet Unit that already holds the logical PID, which is what makes it the same logical PID. What PID_03 does not provide for, and what the paragraphs above supply, is the change of election itself.*

*The encoding of an empty portrait is prescribed by PID_03 in Topic 3 in Annex 2 of the ARF. PID_03 leaves the offering of the opt-out to the discretion of the PID Provider; this provision requires DGEP to offer it to every User.*

*[CIR 2024/2977] makes the inclusion of `portrait` mandatory as of twenty-four months after the entry into force of the Regulation amending it. This Rulebook requires the attribute in every Romanian PID from first issuance; its value is empty under the transitional rule in RO_PID_24, and remains empty for a User who exercises the opt-out in RO_PID_25.*

### 3.3 Example

EXAMPLE: The following shows an [ISO/IEC 18013-5]-compliant Romanian PID, in the CBOR diagnostic notation of [RFC 8949]. It is the same User as the example in Section 4.3 — born in Cluj-Napoca on 12 February 1978, enrolled using an electronic identity card, every attribute value taken from RNEP — so the two examples can be read side by side.

> **UNDER REVIEW — N12, N13.** This example illustrates provisions that are in part withdrawn: its validity, status and binding elements come from Sections 5.2 to 5.4 and Chapter 7. Annex D registers both.

**String values are reproduced exactly as RNEP holds them, which for the names means upper case**, as RO_PID_05 requires. Two values are not reproduced from RNEP and are not upper case: `place_of_birth`, whose form RO_PID_07 fixes, and `issuing_authority`, whose mixed-case value RO_PID_12 fixes.

The attributes and their values in this example:

| Namespace | Attribute identifier | Value |
|---|---|---|
| `eu.europa.ec.eudi.pid.1` | `family_name` | `POPESCU` |
| | `given_name` | `IOAN-ANDREI` |
| | `birth_date` | `1978-02-12` |
| | `place_of_birth` | country `RO`, region `Cluj`, locality `Mun.Cluj-Napoca` |
| | `nationality` | `["RO"]` |
| | `portrait` | empty, per the transitional rule in RO_PID_24 |
| | `expiry_date` | `2030-08-31` |
| | `issuance_date` | `2026-09-01` |
| | `issuing_authority` | `Direcția Generală pentru Evidența Persoanelor` |
| | `issuing_country` | `RO` |
| | `trust_anchor` | `https://<trust-anchor-url>` |
| | `attestation_legal_category` | `PID` |
| `eu.europa.ec.eudi.pid.ro.1` | `personal_numeric_code` | `1780212123451` |
| | `age_over_14` | `true` |
| | `age_over_16` | `true` |
| | `age_over_18` | `true` |
| | `age_over_65` | `false` |

#### The `IssuerSigned` structure

```cbor-diag
{
  "nameSpaces": {
    "eu.europa.ec.eudi.pid.1": [
      24(<<{"digestID": 0, "random": h'8c1f4a90b2e7d3568af0c91d24be7305',
            "elementIdentifier": "family_name", "elementValue": "POPESCU"}>>),
      24(<<{"digestID": 1, "random": h'5d0e7fa3129c46b8e5710da9438fc026',
            "elementIdentifier": "given_name", "elementValue": "IOAN-ANDREI"}>>),
      24(<<{"digestID": 2, "random": h'a91b0c62df84537e10ab29c7605d4e8f',
            "elementIdentifier": "birth_date", "elementValue": 1004("1978-02-12")}>>),
      24(<<{"digestID": 3, "random": h'3e72d5b18096caf4270e6b3d9152a8c0',
            "elementIdentifier": "place_of_birth",
            "elementValue": {"country": "RO", "region": "Cluj",
                             "locality": "Mun.Cluj-Napoca"}}>>),
      24(<<{"digestID": 4, "random": h'c40a91e7523bd68f0ea7143c9d5820b6',
            "elementIdentifier": "nationality", "elementValue": ["RO"]}>>),
      24(<<{"digestID": 5, "random": h'71b8fd0e34a95c26e0d31b7f48a2069c',
            "elementIdentifier": "portrait", "elementValue": h''}>>),
      24(<<{"digestID": 6, "random": h'0f6ac35d9127eb480a3c6d21f85b9740',
            "elementIdentifier": "expiry_date", "elementValue": 1004("2030-08-31")}>>),
      24(<<{"digestID": 7, "random": h'96e1720b4dc8a35f61b09e7d3204ca85',
            "elementIdentifier": "issuance_date", "elementValue": 1004("2026-09-01")}>>),
      24(<<{"digestID": 8, "random": h'2ab7c6019e5d84f37012bc6a95e3d074',
            "elementIdentifier": "issuing_authority",
            "elementValue": "Direcția Generală pentru Evidența Persoanelor"}>>),
      24(<<{"digestID": 9, "random": h'6c093be7a1f5d284b70e5192cd8a4300',
            "elementIdentifier": "issuing_country", "elementValue": "RO"}>>),
      24(<<{"digestID": 10, "random": h'e5804d1a7b93c26520ae7c31d94b6080',
            "elementIdentifier": "trust_anchor",
            "elementValue": "https://<trust-anchor-url>"}>>),
      24(<<{"digestID": 11, "random": h'1d47a9e0538bc6f2904e1ba7c3d56082',
            "elementIdentifier": "attestation_legal_category", "elementValue": "PID"}>>)
    ],
    "eu.europa.ec.eudi.pid.ro.1": [
      24(<<{"digestID": 0, "random": h'b30e51c874926f0158ce3ba9d7402e0f',
            "elementIdentifier": "personal_numeric_code", "elementValue": "1780212123451"}>>),
      24(<<{"digestID": 1, "random": h'd816702ba95e3f4107cd29b640e35a0f',
            "elementIdentifier": "age_over_14", "elementValue": true}>>),
      24(<<{"digestID": 2, "random": h'35e07a1c9d264f80a13e6c795d02b4f0',
            "elementIdentifier": "age_over_16", "elementValue": true}>>),
      24(<<{"digestID": 3, "random": h'7b2094ea6c31d5860e4b12a9c7d3050f',
            "elementIdentifier": "age_over_18", "elementValue": true}>>),
      24(<<{"digestID": 4, "random": h'19d7a5c0e342687b04c19e5a3d762c0f',
            "elementIdentifier": "age_over_65", "elementValue": false}>>)
    ]
  },
  "issuerAuth": [
    h'a10126',                     / protected header: {1: -7} /
    {33: h'3082024a30820…'},       / unprotected header: x5chain /
    h'd8185903f0a7…',              / payload: the tagged MobileSecurityObject below /
    h'9f4d2c07b1e6…'               / signature of DGEP /
  ]
}
```

#### The `MobileSecurityObject`

The payload of `issuerAuth`, shown decoded:

```cbor-diag
{
  "version": "1.0",
  "digestAlgorithm": "SHA-256",
  "valueDigests": {
    "eu.europa.ec.eudi.pid.1": {
      0: h'6f2a91c0e5b7d348a012fe6c39b47d5081ac26e7d90b3f4152ca8067d1e93b24',
      1: h'a1c73e0952d68bf407e1c93ab52d780f64931ec70ab25d8f30146bc9e75a20d3'
      / … digests 2 to 11, one per attribute above … /
    },
    "eu.europa.ec.eudi.pid.ro.1": {
      0: h'3d9e05a7c164b28f70e51ca39d642b087f15ae3c920d6b74015e8ac36d29b407',
      1: h'c8047b1ea395d260f13b7c92a4e05d861079cb3ea2d5468f10e3ba97c52d604b',
      2: h'5b1c93e07af4268d0139ce6b52a7d840e13b9c05af26d738012ce94b6a35d80f',
      3: h'9a41e7c05b3d268f7014ae9c25d6b380f1c0a5e73b9d264802fe1ca75d38b904',
      4: h'742be0c1a95d3f68074ec2b19d5a3608fc17e35b90d24a67013fbe8c25d7a904'
    }
  },
  "deviceKeyInfo": {
    "deviceKey": {
      1: 2,                        / kty: EC2 /
      -1: 1,                       / crv: P-256 /
      -2: h'1bd518cba58475b633542648b0a4ae48a0e5450bd4ca779287459a73929d25e1',
      -3: h'7a09ec56a26648f3234cbab5a747f6a5eacb4e635118e3e77c0c81b709fbab0e'
    }
  },
  "docType": "eu.europa.ec.eudi.pid.1",
  "validityInfo": {
    "signed":     0("2026-09-01T09:12:34Z"),
    "validFrom":  0("2026-09-01T09:12:34Z"),
    "validUntil": 0("2026-11-01T09:12:34Z")
  },
  "status": {
    "status_list": {
      "idx": 274118,
      "uri": "https://<status-list-url>/mdoc/1"
    }
  }
}
```

Notes on the example:

- **`portrait` is present and empty**, as the transitional rule in RO_PID_24 requires. The attribute is not omitted; an empty `bstr` is the encoding RO_PID_25 prescribes.
- **The age assertions are separate attributes**, not one structure, as RO_PID_23 requires, so that a User can disclose `age_over_18` without disclosing the other three. In Section 4.3 the same four are members of one object, individually disclosable under RO_PID_26.
- **`validFrom` and `validUntil` are two months apart in this listing.** The length of the technical validity period is not settled — Sections 5.2 to 5.4 will fix it — so the interval shown is illustrative and is not a requirement of this Rulebook. Both instants fall within the administrative validity period expressed by `issuance_date` and `expiry_date`, as RO_PID_14 requires; that constraint is settled and holds whatever period is fixed. This User's next age-threshold birthday is their sixty-fifth, in 2043, so the age-threshold constraint that Sections 5.2 to 5.4 will place on the technical validity period does not shorten it here; for a User approaching one it would.
- **`status`** references the entry of this technical PID in the Attestation Status List for the [ISO/IEC 18013-5] encoding, which Chapter 7 will route to the mechanism in Annex 2 of [CIR 2024/2979]; that Annex governs the element and its structure. The index is assigned at random, as Chapter 7 will require.
- **`deviceKey` is not the key in the Section 4.3 example.** The two examples are different technical PIDs of the same logical PID, and the uniqueness rule in Sections 5.2 to 5.4 will require every element capable of being unique — including the device-binding public key and every salt and digest — to differ between them. Reading the two examples as one attestation in two encodings would miss the point of issuing technical PIDs in batches.
- **Every URL in this listing is a placeholder and none is an endpoint.** The trust anchor URL is not settled (RO_PID_17; **N9** in Annex D) and the status list URL will be fixed by Chapter 7, so neither is reproduced here.
- The **salts** shown are 16 bytes, as [ISO/IEC 18013-5] requires at minimum, and are real. **The digest values in `valueDigests`, the certificate chain, the payload and the signature are illustrative and are not recomputable from this listing**; the digest map of the `eu.europa.ec.eudi.pid.1` namespace shows two entries and elides the rest, since a digest carries no information about this Rulebook. The attributes, their identifiers and their values are shown in full. **No digest in this listing is recomputable**, here or in `RO_PID_Data_Model.md`, which reproduces it unchanged; the disclosure digests of the [SD-JWT VC] encoding, in Section 3.4 of that document, are real and can be.
- The **signature algorithm** in the protected header is `-7`, that is ECDSA with P-256 and SHA-256, and the `deviceKey` is a P-256 key. Both are what RO_PID_55 requires, as is the SHA-256 in `digestAlgorithm`.

---

## 4 SD-JWT VC-based encoding of the Romanian PID

This chapter specifies the encoding of the Romanian PID where it complies with [SD-JWT VC]. This encoding is used principally for remote presentation.

### 4.1 Encoding of PID attributes and metadata

Following requirement ARB_06b of the ARF, [SD-JWT VC]-encoded PIDs use claim names that are registered in the JSON Web Token Claims Registry [IANA-JWT-Claims], are Public Names as defined in [RFC 7519], or are Private Names specific to the attestation type.

A [SD-JWT VC]-compliant Romanian PID SHALL comply with the *IETF SD-JWT VC Profile* specified in Section 6.1 of [HAIP], as requirement ARB_01b in Topic 12 in Annex 2 of the ARF requires. Where that profile constrains a matter this chapter leaves open, the profile governs.

A JSON string in a Romanian PID SHALL be encoded in UTF-8 and SHALL support the full Unicode range. Romanian diacritics SHALL be preserved and SHALL NOT be transliterated.

A hierarchical claim name structure is used, written `parent.child` where this Rulebook refers to a nested claim, as it does for the members of `place_of_birth`. [SD-JWT VC] allows individual selective disclosure of objects and of their properties.

The standard JWT claims `nbf` and `exp` express the technical validity period of a [SD-JWT VC]-compliant Romanian PID. They are distinct from `date_of_issuance` and `date_of_expiry`, which express the administrative validity period of the logical PID; see the note in Section 2.5.

#### 4.1.1 IANA-registered claim names

| Data Identifier | Claim name | Encoding format | Reference | Inclusion |
|---|---|---|---|---|
| family_name | `family_name` | string | Section 5.1 of [OIDC] | SHALL |
| given_name | `given_name` | string | Section 5.1 of [OIDC] | SHALL |
| birth_date | `birthdate` | string, [ISO 8601-1] `YYYY-MM-DD` format | Section 5.1 of [OIDC] | SHALL |
| birth_place | `place_of_birth` | JSON structure; at least one of `country`, `region` or `locality` SHALL be present. What each member carries is governed by RO_PID_07 | Section 4.1 of [EKYC] | SHALL |
| nationality | `nationalities` | array of strings, alpha-2 country codes | Section 4.1 of [EKYC] | SHALL |
| portrait | `picture` | string; data URL containing the base64-encoded portrait in JPEG format, subject to RO_PID_24 | Section 5.1 of [OIDC] | SHALL |
| resident_address | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| resident_country | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| resident_state | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| resident_city | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| resident_postal_code | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| resident_street | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| family_name_birth | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| given_name_birth | — | not encoded | — | SHALL NOT, per RO_PID_11 |
| email_address | `email` | string | Section 5.1 of [OIDC] | SHALL NOT, per RO_PID_09 |
| mobile_phone_number | `phone_number` | string | Section 5.1 of [OIDC] | SHALL NOT, per RO_PID_09 |

#### 4.1.2 Private Names specific to the attestation type

| Data Identifier | Claim name | Encoding format | Inclusion |
|---|---|---|---|
| expiry_date | `date_of_expiry` | string, [ISO 8601-1] `YYYY-MM-DD` format, as defined in Section 5.4.4.2 of [EKYC Schema] | SHALL |
| issuance_date | `date_of_issuance` | string, [ISO 8601-1] `YYYY-MM-DD` format, as defined in Section 5.4.4.2 of [EKYC Schema] | SHALL |
| sex | — | not encoded | SHALL NOT, per RO_PID_11 |
| resident_house_number | — | not encoded | SHALL NOT, per RO_PID_11 |
| issuing_authority | `issuing_authority` | string | SHALL |
| issuing_country | `issuing_country` | string | SHALL |
| personal_administrative_number | `personal_administrative_number` | string | SHALL NOT, per RO_PID_10 |
| document_number | `document_number` | string | SHALL NOT, per RO_PID_15 |
| issuing_jurisdiction | `issuing_jurisdiction` | string | SHALL NOT, per RO_PID_16 |
| trust_anchor | `trust_anchor` | string | SHALL |
| attestation_legal_category | `attestation_legal_category` | string | SHALL |

#### 4.1.3 Romanian domestic claims

| Data Identifier | Claim name | Encoding format | Inclusion |
|---|---|---|---|
| personal_numeric_code | `personal_numeric_code` | string, exactly 13 decimal digits | SHALL |
| age_equal_or_over | `age_equal_or_over` | JSON object with four boolean members, one per threshold; see RO_PID_27 | SHALL, per RO_PID_20 |

**RO_PID_26** — In a [SD-JWT VC]-compliant Romanian PID, all claims SHALL be individually selectively disclosable — every top-level property, every nested property, and every array entry alike — except those claims that [SD-JWT VC] defines as non-selectively disclosable, and except `iat`.

This applies in particular to the members of `place_of_birth`; to the four members of `age_equal_or_over`; and to the entries of the `nationalities` array. A Wallet Unit SHALL be able to present any one of them without presenting the structure or array in which it sits.

*Transposes requirement PID_21 in Topic 3 in Annex 2 of the ARF. The claims [SD-JWT VC] excepts are not enumerated here; that specification identifies them. `iat` is excepted by this provision and not by [SD-JWT VC], which leaves it disclosable at the issuer's option: it dates the technical PID rather than conveying an attribute of the User, which is the character the other excepted claims share.*

**RO_PID_27** — The `age_equal_or_over` claim SHALL be a JSON object whose members are the age thresholds defined in RO_PID_20, each expressed as a decimal string and each taking a JSON boolean value:

```json
{
  "age_equal_or_over": {
    "14": true,
    "16": true,
    "18": true,
    "65": false
  }
}
```

The example above shows the claim as it appears within the payload; the enclosing braces are the payload's and are not part of the claim.

All four members SHALL be present, whether true or false. Each SHALL be individually selectively disclosable under RO_PID_26.

*The member names are strings and not numbers, because a JSON object key is a string by definition. A Relying Party SHALL NOT rely on the ordering of the members.*

*The claim is not encoded as four flat claims matching the [ISO/IEC 18013-5] attribute identifiers of Section 3.1.5. The object is the form the EU instruments use for this claim, and RO_PID_23 records that the structural difference between the two encodings is not to be reconciled.*

### 4.2 Verifiable Credential Type and Type Metadata

[SD-JWT VC] defines the Verifiable Credential Type, `vct`. A type carries associated metadata that provides information about the type, outlines a schema detailing which claims are optional and which mandatory, and specifies their display. A type can extend another type, which enables a domestic type to be built on a common EU-wide type while preserving the mandatory claims of the base type.

Requirement PID_14 in Topic 3 in Annex 2 of the ARF defines the base type as `urn:eudi:pid:1`. As a convention, all PIDs must use types in the namespace `urn:eudi:pid:`.

**RO_PID_28** — A [SD-JWT VC]-compliant Romanian PID SHALL use the Verifiable Credential Type `urn:eudi:pid:ro:1`. That type SHALL extend `urn:eudi:pid:1` and SHALL preserve every mandatory claim of the base type.

**RO_PID_29** — DGEP SHALL author and publish Type Metadata for `urn:eudi:pid:ro:1`. The Type Metadata SHALL be consistent with this Rulebook; where they diverge, this Rulebook prevails and the Type Metadata is corrected.

The `display` array of that Type Metadata SHALL carry entries for at least Romanian and English, identified by the `lang` member, whose value is a language tag as specified in [BCP 47], covering the attestation type itself and the domestic claims defined in Section 4.1.3. The English rendering of the name of the PID Provider SHALL be identical to the one carried in the Credential Issuer Metadata DGEP publishes.

That Type Metadata SHALL further carry the Claim Selective Disclosure Metadata defined in Section 9.3 of [SD-JWT VC] for every claim of a Romanian PID, expressing the rule stated in RO_PID_26.

*Requirement ARB_31 in Topic 12 in Annex 2 of the ARF recommends this; it is mandatory here. Where the Type Metadata and RO_PID_26 do not agree, RO_PID_26 governs and the Type Metadata is corrected.*

**RO_PID_30** — DGEP SHALL publish this Rulebook in the catalogue of attestation rulebooks, complying with the applicable requirements of Topic 12 in Annex 2 of the ARF.

Where an attestation scheme for the Romanian PID is registered in the catalogue of attestation schemes established under Article 8 of [CIR 2025/1569], that registration SHALL reference this Rulebook, as requirement ARB_33 requires.

*Requirements PID_07 and PID_16 in Topic 3 require a PID Provider that defines a domestic namespace or a domestic type to publish it, with all attribute or claim identifiers, their definitions, presence and encoding format, in an Attestation Rulebook complying with Topic 12. This Rulebook is that Attestation Rulebook, and Sections 2.7, 3.1.5 and 4.1.3 are that publication.*

### 4.3 Example

EXAMPLE: The following shows the payload of a Romanian PID in [SD-JWT VC] format before encoding into the SD-JWT format. The User in this example was born in Cluj-Napoca on 12 February 1978 and enrolled using their electronic identity card. Every attribute value shown is taken from RNEP: the CEI is used for onboarding and is not a source of attribute values, as RO_PID_04 provides.

> **UNDER REVIEW — N12, N13.** As with Section 3.3, this example illustrates provisions that are in part withdrawn: its validity, status and binding elements come from Sections 5.2 to 5.4 and Chapter 7. Annex D registers both.

**String values are reproduced exactly as RNEP holds them, which for the names means upper case**, as RO_PID_05 requires. Two values are not reproduced from RNEP and are not upper case: `place_of_birth`, whose form RO_PID_07 fixes, and `issuing_authority`, whose mixed-case value RO_PID_12 fixes.

```json
{
  "iss": "https://<credential-issuer>",
  "vct": "urn:eudi:pid:ro:1",

  "iat": 1788253954,
  "nbf": 1788253954,
  "exp": 1793524354,

  "family_name": "POPESCU",
  "given_name": "IOAN-ANDREI",
  "birthdate": "1978-02-12",

  "place_of_birth": {
    "country": "RO",
    "region": "Cluj",
    "locality": "Mun.Cluj-Napoca"
  },

  "nationalities": ["RO"],

  "picture": "",

  "personal_numeric_code": "1780212123451",

  "age_equal_or_over": {
    "14": true,
    "16": true,
    "18": true,
    "65": false
  },

  "date_of_issuance": "2026-09-01",
  "date_of_expiry": "2030-08-31",

  "issuing_authority": "Direcția Generală pentru Evidența Persoanelor",
  "issuing_country": "RO",
  "attestation_legal_category": "PID",
  "trust_anchor": "https://<trust-anchor-url>",

  "status": {
    "status_list": {
      "idx": 412703,
      "uri": "https://<status-list-url>/sd-jwt/1"
    }
  },

  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "52aDI_ur05n1f_p3jiYGUU82oKZr3m4LsAErM536crQ",
      "y": "ckhZ-KQ5aXNL91R8Eufg1aOf8Z5pZJnIvuCzNGfdnzo"
    }
  }
}
```

Notes on the example:

- The **`cnf`** claim expresses key binding, and holds the public key of the key pair whose private key is held in the WSCD of the Wallet Unit, as the device-binding rule in Sections 5.2 to 5.4 will require.
- **`nbf`** and **`exp`** express the technical validity period. Here they are 1 September 2026 at 09:12:34 UTC and 1 November 2026 at the same time. The length of that period is not settled — Sections 5.2 to 5.4 will fix it — so the two months shown are illustrative and are not a requirement of this Rulebook. `date_of_issuance` and `date_of_expiry` express the administrative validity period of the logical PID, and the technical period is contained within it as RO_PID_14 requires. This User's next age-threshold birthday is their sixty-fifth, in 2043, so the age-threshold constraint that Sections 5.2 to 5.4 will place on the technical validity period does not shorten it here; for a User approaching one it would.
- **`status`** references the entry of this technical PID in the Attestation Status List Chapter 7 will provide for, in the form [Token Status List] specifies. The index is assigned at random, as Chapter 7 will require.
- **`picture`** is present and empty, as the transitional rule in RO_PID_24 requires. An empty JSON string is the encoding RO_PID_25 prescribes. Once the attribute is populated it carries the whole base64-encoded JPEG in a `data:` URL, subject to the quality constraints of RO_PID_24 and to any constraint on the encoded size added there.
- **Every URL in this listing is a placeholder and none is an endpoint.** The trust anchor URL is not settled (RO_PID_17; **N9** in Annex D) and the status list URL will be fixed by Chapter 7, so neither is reproduced here. The Credential Issuer identifier is not fixed by this Rulebook at all: it is published in the Credential Issuer Metadata and notified as a service supply point under RO_PID_53.
- Every claim shown is individually selectively disclosable under RO_PID_26, including each member of `place_of_birth` and each of the four members of `age_equal_or_over`, except those claims that [SD-JWT VC] itself defines as non-selectively-disclosable.

Note: `personal_numeric_code` is the only persistent identifier in the attestation, and, read on its own, it discloses that the User is male, was born on 12 February 1978, and was registered in the county whose code is 12 — which is why Section 5.4 will restrict when it may be requested. It is the one claim in this example that discloses materially more than it appears to: `age_equal_or_over` was included precisely so that a Relying Party needing an age check need not request `birthdate`, and requesting the CNP instead would obtain the date of birth anyway.

---

## 5 PID usage

Users request issuance of Romanian PIDs from DGEP, manage them in their Wallet Unit, and present attributes from a PID to Relying Parties on request. DGEP issues Romanian PIDs to Wallet Units on request of Users, and revokes them if necessary. Relying Parties request attributes from a User's PID and verify their authenticity and validity, including revocation status.

Users, DGEP, and Relying Parties do this in compliance with all applicable requirements in the European Digital Identity Regulation and the corresponding Implementing Acts, as described in the ARF.

**Section 5.1 is in force. Sections 5.2 to 5.4 are withdrawn pending decision**, as Annex D records at **N12**.

### 5.1 Enrolment and issuance

**RO_PID_31** — DGEP SHALL issue a logical Romanian PID only after identity proofing and verification meeting the requirements for assurance level **high** set out in [CIR 2015/1502]. Enrolment SHALL follow the process below, which combines an electronic step performed by the User remotely with an in-person confirmation. It is a **single channel**: neither part alone is sufficient.

| # | Step |
|---|---|
| 1 | The User installs RO Wallet and starts an enrolment request from it. |
| 2 | The User presents their CEI to the device over its contactless interface. RO Wallet reads the card and requests the authentication PIN of that CEI, which the User enters. |
| 3 | RO Wallet transmits the resulting proof that the User possesses and controls the CEI to DGEP. Where DGEP accepts it, DGEP SHALL record a **pending enrolment** and RO Wallet SHALL inform the User that the enrolment is to be completed in person at an MoIA counter. |
| 4 | At the counter, a member of staff compares the User against the CEI they present, and opens the registration function, which displays a QR code. |
| 5 | The User scans that QR code with RO Wallet. This SHALL establish that the Wallet Unit completing the enrolment is the Wallet Unit that began it at step 1. |
| 6 | The system retrieves the record of the User from RNEP, including the facial image, and displays it to the member of staff, who compares it against the User and against the CEI presented. The member of staff confirms the identity only where all three agree. |
| 7 | On confirmation the system generates a second, **short-lived** QR code, refreshed at intervals of a few seconds and valid for no more than one minute. |
| 8 | The User scans that second QR code with RO Wallet. This SHALL again establish that the Wallet Unit is the one that began the enrolment, and SHALL constitute the User's authorisation to proceed. |
| 9 | RO Wallet requests issuance, and DGEP issues the logical Romanian PID. |

DGEP SHALL NOT issue a Romanian PID on the basis of a self-asserted identity, or of a document that is expired or reported lost or stolen. DGEP SHALL NOT complete an enrolment in which the identity confirmation at step 6 was not performed.

**DGEP SHALL issue a Romanian PID to a Wallet Unit of any Wallet Solution recognised under the corresponding notified electronic identification scheme**, on request of the User. The process above is written in terms of RO Wallet because it is the first such Wallet Solution, and does not limit this duty; where another Wallet Solution is recognised, DGEP SHALL make an equivalent process available to its Wallet Units.

**DGEP SHALL publish the list of Wallet Solutions from which it accepts a request for a Romanian PID**, in such a way that a prospective User can readily find it.

*Transposes requirements ISSU_19a and ISSU_20 in Topic 10 in Annex 2 of the ARF. ISSU_20 is a policy requirement rather than a technical one, and the ARF contemplates publication on the PID Provider's website.*

*The two scans at steps 5 and 8 are what bind the PID to the device: the first establishes that the Wallet Unit at the counter is the one that read the CEI, and the second that the User authorised issuance from it while present. Without them the in-person confirmation would establish who the User is but not which device receives the attestation.*

*The electronic step at steps 2 and 3 establishes that the User possesses the CEI and controls its authentication PIN. It is not relied on as an electronic identification means, and nothing in this provision turns on whether any national scheme has been notified at a given level: the identity proofing on which the level of assurance in RO_PID_02 rests is the comparison of the User against the CEI and against the RNEP record, performed in person at step 6.*

*[CIR 2015/1502] is the instrument that defines assurance levels for electronic identification means. The note to WIAM_14b in Topic 40 in Annex 2 of the ARF records that the term 'level of assurance', as used in the European Digital Identity Regulation and in [CIR 2015/1502], applies in the EUDI Wallet context to the PID.*

**RO_PID_32** — A Wallet Unit obtaining a Romanian PID SHALL support a process to activate it, in accordance with the requirements for assurance level high in [CIR 2015/1502] Section 2.2.2, and SHALL NOT allow a User to use a Romanian PID that has not been activated. RO Wallet SHALL support that process; where a Wallet Unit of another Wallet Solution obtains a Romanian PID under RO_PID_31, it is bound by this provision on the same terms.

For a Romanian PID, activation is performed by the two scans at **steps 5 and 8** of RO_PID_31, which together establish that the Wallet Unit completing the enrolment is the one that began it and that the User authorised issuance from it while present. Issuance itself follows at step 9. That is the outcome [CIR 2015/1502] Section 2.2.2 requires and which ISSU_05 exists to secure: the attestation reaches the Wallet Unit and the Wallet Secure Cryptographic Device of the User who is its subject.

*Transposes requirement ISSU_05 in Topic 10 in Annex 2 of the ARF, which cites that Section.*

### 5.2 to 5.4 — Technical PID lifecycle, presentation, and restrictions on requesting attributes

*To be established — under analysis.*

> **UNDER REVIEW — N12.** These sections are not settled and their content is withdrawn pending decision. They will govern the **issuance protocol**; the **lifecycle** of a technical PID, including technical validity, batching, single use, replenishment, re-issuance and deletion; **presentation and selective disclosure**; and the **restrictions on requesting** the national identification number.
>
> The identifiers **RO_PID_33 to RO_PID_52** are reserved for them. A reference to any of them made elsewhere in this Rulebook is a reference to the provision as it will be settled.

---

## 6 Trust anchors

PID trust anchors are public keys and associated information, needed by Relying Parties to verify the authenticity of any PID attributes they obtain from Wallet Units.

**RO_PID_53** — Romania SHALL notify DGEP as a PID Provider to the Commission as specified in the European Digital Identity Regulation and [CIR 2024/2980], using the common system provided by the Commission and complying with the applicable requirements of [Technical Specification 2]. Relying Parties retrieve the trust anchors of DGEP from the List of Trusted Entities of PID Providers published by the Commission.

That notification SHALL include at least the following, as requirement PPNot_02 in Topic 31 in Annex 2 of the ARF requires:

| # | Notified information |
|---|---|
| 1 | Identification data for DGEP: Romania as the Member State of establishment, the name of record *Direcția Generală pentru Evidența Persoanelor*, and, where applicable, the registration number and identification data of the official record in which it is registered. |
| 2 | The trust anchors of DGEP supporting the authentication of Romanian PIDs. |
| 3 | The trust anchors supporting the authentication of the Attestation Status Lists provided for in Chapter 7. These are distinct from the trust anchors in row 2. |
| 4 | The trust anchors of the Access Certificate Authorities issuing access certificates to DGEP, supporting the authentication of DGEP by Wallet Units at the service supply points in row 5. |
| 5 | The service supply point or points: the URL or URLs at which a Wallet Unit can begin the process of requesting and obtaining a Romanian PID. |
| 6 | The URL at which Relying Parties and other entities can retrieve the Attestation Status Lists, as Chapter 7 will require and as requirement ARB_24a in Topic 12 in Annex 2 of the ARF requires. |

DGEP SHALL ensure that every Romanian PID it issues can be authenticated using the trust anchors notified under row 2; that every Attestation Status List used to revoke a Romanian PID can be authenticated using the trust anchors notified under row 3; and that its access certificates can be authenticated using the Access Certificate Authority trust anchors notified under row 4.

*Requirements PPNot_03, PPNot_03a and PPNot_04 impose the three assurances in the paragraph above. The trust anchor that authenticates a status list is not the trust anchor that signs a PID.*

The **List of Trusted Entities of PID Providers**, compiled by the Commission from the notifications made under this provision and published at `https://eidas.ec.europa.eu/efda/wallet/lists-of-trusted-entities/pid-providers`, is the authoritative source of the trust anchors of DGEP. A Relying Party verifying a Romanian PID SHALL obtain those trust anchors from that list. The URL carried in the `trust_anchor` attribute under RO_PID_17 is a convenience and does not displace it; a Relying Party SHALL NOT rely on a trust anchor obtained from that URL alone where the List of Trusted Entities is available to it.

*[PID Rulebook] Section 6 refers to a Trusted List. The trust anchors of notified PID Providers are in fact published in a List of Trusted Entities complying with [ETSI TS 119 602], as requirements PPNot_05 and PPNot_07 in Annex 2 of the ARF provide and as the published list shows. This Rulebook follows the list that exists.*

**Registration is distinct from notification, and both are required.** In addition to the notification above, DGEP SHALL be registered in the Romanian registry of PID Providers established under Topic 27 in Annex 2 of the ARF. DGEP SHALL register one or more Services and, for each, the type or types of attestation that Service intends to issue to Wallet Units; for every Service issuing the Romanian PID, that SHALL include the Romanian PID. DGEP SHALL make any update necessary to keep the registered information correct, without undue delay.

*The two duties above are requirements Reg_10e and Reg_08 in Topic 27 in Annex 2 of the ARF. Registration causes a registration certificate to be issued under RPRC_13, whose contents RPRC_15 governs and which DGEP publishes in its Credential Issuer Metadata. The vetting of PID Providers and the maintenance of the registry are the Member State's under Reg_19 and Reg_20.*

**RO_PID_54** — The private keys used by DGEP to sign Romanian PIDs SHALL be generated and held in a hardware security module certified to at least **FIPS 140-3 Level 3** or **Common Criteria EAL4+**, SHALL NOT be exportable from that module in plaintext, and SHALL be subject to a documented lifecycle covering generation, activation, rotation, revocation, and destruction. **DGEP SHALL operate that infrastructure.**

Rotation of a signing key SHALL NOT invalidate technical PIDs already issued under the superseded key for the remainder of their technical validity period, and DGEP SHALL keep the corresponding trust anchor available for that period.

### 6.1 Cryptographic algorithms

**RO_PID_55** — DGEP, RO Wallet and Relying Parties SHALL use only cryptographic algorithms included in the [ECCG Agreed Cryptographic Mechanisms] when issuing, presenting or verifying a Romanian PID, a Wallet Instance Attestation or a Key Attestation.

A Romanian PID SHALL use at least the following:

| Purpose | Algorithm |
|---|---|
| The DGEP signature over a technical PID — the `issuerAuth` signature of an [ISO/IEC 18013-5]-compliant PID, and the issuer signature of a [SD-JWT VC]-compliant PID | **ECDSA with curve P-256 and SHA-256** |
| Device binding — mdoc authentication in [ISO/IEC 18013-5], key binding in [SD-JWT VC] | **ECDSA with curve P-256 and SHA-256** |
| The digests of attribute values in the Mobile Security Object of an [ISO/IEC 18013-5]-compliant PID, and the disclosure digests of a [SD-JWT VC]-compliant PID | **SHA-256** |

DGEP MAY publish, in a technical profile, further algorithms that a Romanian PID may use for any of those purposes. Every algorithm so published SHALL be included in the [ECCG Agreed Cryptographic Mechanisms]. DGEP SHALL NOT publish a profile that removes an algorithm required above while any technical PID using it remains within its technical validity period.

*The first paragraph transposes requirement OIA_03 in Topic 1 and requirement WUA_04 in Topic 9 in Annex 2 of the ARF. Neither requirement selects an algorithm; both constrain the set one may be selected from.*

*The [ECCG Agreed Cryptographic Mechanisms] is maintained outside this Rulebook and is one of the instruments RO_PID_61 requires this Rulebook to be reviewed against.*

---

## 7 Revocation

*To be established — under analysis.*

> **UNDER REVIEW — N13.** This chapter is not settled and its content is withdrawn pending decision. It will govern the **publication of revocation status**, the operation of the lists carrying it, the **cascade** from a revoked logical PID to the technical PIDs derived from it, **revocation checking** by Relying Parties, and the **grounds** on which DGEP revokes.
>
> The identifiers **RO_PID_56 to RO_PID_60** are reserved for this chapter. A reference to any of them made elsewhere in this Rulebook is a reference to the provision as it will be settled.

---

## 8 Compliance

This Rulebook is drafted to comply with all applicable requirements in Topic 12 (Attestation Rulebooks) in Annex 2 of the ARF, and to follow the template for Attestation Rulebooks as ARB_29 recommends.

**What has been assessed, and what has not.** Conformance with Topic 3 is recorded requirement by requirement in **Annex B**, and conformance with Topic 12 and with the template in **Annex C**, each against the revision stated in it. The assertion in the paragraph above is therefore evidenced and not merely made.

**It does not presently hold in full.** Chapter 7 is withdrawn in full, as are Sections 5.2 to 5.4, as Annex D records, and the requirements they transposed are consequently not transposed. Annexes B and C mark every affected row. This Rulebook is not in a state in which it can be notified or assessed as a whole, and Annex D is the list of what has to be settled before it is.

Those requirements of Annex 2 outside Topics 3 and 12 that bear on a PID Provider have been assessed against the same revision. Requirements identified in the course of that assessment as not yet transposed are recorded outside this Rulebook, and RO_PID_61(d) requires the assessment to be maintained.

**This Rulebook is the Attestation Rulebook required by PID_07 and PID_16** in Topic 3 in Annex 2 of the ARF. PID_07 requires a PID Provider that defines a domestic namespace to publish it, with all attribute identifiers, their definitions, presence and encoding format; Section 2.7 and Section 3.1.5 are that publication. PID_16 requires the equivalent for a domestic type; Section 2.7 and Section 4.1.3 are that publication. RO_PID_30 requires this Rulebook to be published in the catalogue of attestation rulebooks.

PID_06 defines the domestic namespace by reference to ARB_10 in Topic 12, which applies Topic 12's namespace requirements to domestic namespaces. The operative one is ARB_06a: the namespace identifier `eu.europa.ec.eudi.pid.ro.1` is unique within the EUDI Wallet ecosystem by construction, the five domestic attribute identifiers are mutually distinct, and Sections 2.7 and 3.1.5 define the semantics and the syntax of each.

The attributes specified in Chapter 2 comply with [CIR 2024/2977]. The domestic attributes specified in Section 2.7 are defined in accordance with requirement PID_06 in Topic 3 in Annex 2 of the ARF.

The encodings specified in Chapters 3 and 4 comply with [PID Rulebook] version 1.7, with [ISO/IEC 18013-5] and with [SD-JWT VC] respectively. Where this Rulebook is more restrictive than [PID Rulebook] — in requiring `full-date` for `expiry_date` and `issuance_date`, and in requiring attributes that [PID Rulebook] makes optional — it restricts a choice that [PID Rulebook] leaves open, and does not permit anything [PID Rulebook] forbids.

**This Rulebook declines every optional attribute of [CIR 2024/2977], and two of its four optional metadata elements.** RO_PID_09, RO_PID_10 and RO_PID_11 state the attributes declined; RO_PID_15 and RO_PID_16 decline `document_number` and `issuing_jurisdiction`, while Section 2.5 makes `expiry_date` and `issuance_date` mandatory here. Each is optional under [CIR 2024/2977], and whether to issue an optional attribute is a choice reserved to the Member State, so declining all of them is not a departure from that Regulation and is not a departure from [PID Rulebook], which reproduces the same optional set. Every declined attribute appears in the tables of Chapter 2 with the reason stated, so that the chapter remains a complete account of what a Romanian PID does and does not carry.

The Romanian PID therefore carries the six mandatory attributes and the two mandatory metadata elements of [CIR 2024/2977]; `expiry_date` and `issuance_date`, which [CIR 2024/2977] makes optional and the table in Section 2.5 makes mandatory here, RO_PID_13 fixing how `expiry_date` is computed; the two additional attributes of [PID Rulebook] that Section 2.6 makes mandatory, of which RO_PID_17 fixes the value of `attestation_legal_category`, that of `trust_anchor` being unsettled under N9; and the domestic attributes of Section 2.7.

The domestic attributes rest on a different requirement in each encoding, and the two are not interchangeable. **PID_06 governs the [ISO/IEC 18013-5] encoding**, sitting among the requirements for [ISO/IEC 18013-5]-compliant PIDs: it permits a PID Provider to include attributes not defined in [PID Rulebook] provided they sit in a domestic namespace constructed as that requirement prescribes, which is what Sections 2.7 and 3.1.5 do. **PID_14 and PID_16 govern the [SD-JWT VC] encoding**, where there are no namespaces: PID_14 permits a domestic Verifiable Credential Type extending `urn:eudi:pid:1`, which RO_PID_28 defines, PID_16 requires its claims to be published in an Attestation Rulebook, which Section 4.1.3 does, and ARB_06b constrains how the claim names are formed. This applies in particular to the age assertions in `age_equal_or_over`: age attributes were removed from [PID Rulebook] at its version 1.1, so they are not attributes of the EU-wide PID, and carrying them domestically is what these requirements exist to allow. The unique identifier of the Romanian PID is the CNP, carried as a domestic attribute under RO_PID_19, and the processing policy governing it is a matter of national law.

Requirement ARB_22 obliges this Rulebook to specify all technical details necessary to ensure the interoperability, security and privacy of the Romanian PID. So far as interoperability and security are concerned, the operative provision is RO_PID_55, which fixes the cryptographic algorithms a Romanian PID uses; without it a party building against this Rulebook would have to select an algorithm for itself, and two such parties could conform to this Rulebook and still fail to interoperate. So far as privacy is concerned, the operative provisions were those governing the uniqueness of per-attestation elements and the operation of the status lists, which are withdrawn with Sections 5.2 to 5.4 and Chapter 7; ARB_22 is accordingly only partly satisfied at present. Requirement ARB_02 is addressed in the opening of Chapter 3, ARB_09 in Section 2.1, ARB_30 in RO_PID_26, ARB_31 in RO_PID_29, and ARB_33 in RO_PID_30. ARB_23, ARB_24a, ARB_28 and ARB_34 were addressed by provisions now withdrawn; Annex C records the position on each.

Further requirements in this Rulebook comply with or reference the applicable requirements in the ARF and the relevant Implementing Acts.

### 8.1 Maintaining conformance

**RO_PID_61** — **DGEP SHALL review this Rulebook against the instruments on which it depends**, as its author and maintainer. The following apply.

- **(a) Instruments.** The instruments are: [PID Rulebook]; Topics 1, 3, 6, 7, 9, 10, 11, 12, 24, 25, 27, 31, 34, 38, 40, 44 and 51 in Annex 2 of the ARF; the [Rulebook template]; [ISO/IEC 18013-5] and [SD-JWT VC], which Chapters 3 and 4 profile; [OpenID4VCI]; [Technical Specification 2] and [Technical Specification 3]; [ECCG Agreed Cryptographic Mechanisms]; [HAIP], [Token Status List], [ETSI TS 119 602], [ETSI TS 119 471], [ETSI TS 119 412-6] and [ETSI TS 119 472-3]; [OIDC], [EKYC], [EKYC Schema] and [IANA-JWT-Claims], from which Chapter 4 takes its claim names; [ISO/IEC 39794-5] and [ISO/IEC 19794-5], which govern the portrait; [Reg. eIDAS 2], [CIR 2015/1502], [CIR 2024/2977], [CIR 2024/2979], [CIR 2024/2980], [CIR 2024/2982] and [CIR 2025/1569]; and [OUG 97/2005] and [Law 119/1996], on which RO_PID_19 rests. **This list is not every instrument this Rulebook cites.** It is those whose revision could require this Rulebook to be amended: the instruments this Rulebook profiles or restates, and those from which it takes a requirement, a permitted set, a claim name or a value. Chapter 9 lists every instrument cited, and an instrument cited there but not here is one cited only for a definition, a code set, a character set, a date or data format, or a notation, whose revision does not bear on the provisions of this Rulebook. **Nor is the list limited to what this Rulebook cites.** A Topic in Annex 2 of the ARF that bears on a PID Provider is reviewed whether or not this Rulebook presently cites it, because a revision of it may create a dependency where none exists today; RO_PID_61(d) requires the assessment outside Topics 3 and 12 on the same footing. Where a review or an amendment introduces a dependency of the first kind on a further instrument, it SHALL be added to this list in the same version. A review SHALL verify that every entry in this list resolves to an instrument that exists, that every instrument in Chapter 9 which is not listed here still meets the criterion for omission, and that every requirement this Rulebook cites is located in the topic or section this Rulebook attributes it to.
- **(b) Trigger.** On publication of a new version of any of them, DGEP SHALL perform a review without undue delay, and in any event **within three months** of that publication.
- **(c) Backstop.** Irrespective of whether any such publication has been observed, DGEP SHALL perform a review **at least once every twelve months**.
- **(d) Scope.** Each review SHALL re-perform the conformance assessments recorded in Annex B and in Annex C; re-perform the equivalent assessment against those requirements of Annex 2 outside Topics 3 and 12 that bear on a PID Provider, and complete it where it has not yet been recorded; verify that the provisions of this Rulebook which restate the content of an instrument still match that instrument; and verify that every cross-reference to an external requirement still resolves and still states what this Rulebook attributes to it. Each review SHALL also verify that `RO_PID_Data_Model.md` still agrees with every provision it restates — Chapters 2, 3 and 4, and what it carries from Chapter 1 and Section 6.1 — and correct it where it does not.
- **(e) Record.** On completion of every review, DGEP SHALL update the baseline dates recorded in the version history, **whether or not the review resulted in any change to this Rulebook**. The version history is the only place in this Rulebook where an assessment baseline date is recorded. The versions of the instruments themselves are stated there and repeated in Chapter 9 and in Annex C, and a review SHALL keep the three consistent.
- **(f) Outcome.** Where a review identifies a divergence, DGEP SHALL issue a new version of this Rulebook correcting it.

*The two intervals this provision fixes are the **three months** in (b), within which a review follows the publication of a new version of an instrument, and the **twelve months** in (c), the backstop that runs irrespective of any publication. Neither is derived from a Romanian or an EU requirement; both are national choices.*

---

## 9 References

| Reference | Document |
|---|---|
| **[Reg. eIDAS 2]** | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework. |
| **[CIR 2015/1502]** | Commission Implementing Regulation (EU) 2015/1502 setting out minimum technical specifications and procedures for assurance levels for electronic identification means. |
| **[CIR 2024/2977]** | Commission Implementing Regulation (EU) 2024/2977 on person identification data and electronic attestations of attributes. |
| **[CIR 2024/2979]** | Commission Implementing Regulation (EU) 2024/2979 on the core functionality of the European Digital Identity Wallet. |
| **[CIR 2024/2980]** | Commission Implementing Regulation (EU) 2024/2980 on the notification to the Commission of electronic identification schemes and of providers. |
| **[CIR 2024/2982]** | Commission Implementing Regulation (EU) 2024/2982 on protocols and interfaces. |
| **[CIR 2025/1569]** | Commission Implementing Regulation (EU) 2025/1569. Article 8 establishes the catalogue of schemes for the attestation of attributes. |
| **[OUG 97/2005]** | *Ordonanța de urgență a Guvernului* no. 97/2005 on the records, domicile, residence and identity documents of Romanian citizens, republished as amended. Article 6 establishes the CNP. |
| **[Law 119/1996]** | *Legea* no. 119/1996 on civil status documents, republished as amended. Article 22(1) bears on the assignment of the CNP from birth. |
| **[ARF]** | European Digital Identity Wallet — Architecture and Reference Framework. |
| **[PID Rulebook]** | PID Rulebook, ARF Annex 3.01, version 1.7, 17 July 2026, maintained in the EUDI Wallet attestation rulebooks catalogue. |
| **[Rulebook template]** | The template for Attestation Rulebooks, version 1.5, 8 July 2026. Requirement ARB_29 in Topic 12 in Annex 2 of the ARF recommends following its structure and contents; Annex C.2 records how this Rulebook does. |
| **[ISO/IEC 18013-5]** | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application. |
| **[SD-JWT VC]** | SD-JWT-based Verifiable Credentials. |
| **[Token Status List]** | Token Status List, the mechanism referenced by requirement VCR_11a in Topic 7 in Annex 2 of the ARF for the revocation of [SD-JWT VC]-compliant attestations. |
| **[ETSI TS 119 602]** | ETSI TS 119 602, Trusted lists — Data model for Lists of Trusted Entities. The format of the List of Trusted Entities of PID Providers from which a Relying Party obtains the trust anchors of DGEP, per requirement PPNot_07 in Topic 31 in Annex 2 of the ARF. |
| **[ETSI TS 119 471]** | ETSI TS 119 471, Policy and security requirements for Attestation Providers. Requirement ISSU_67 in Topic 10 in Annex 2 of the ARF requires a PID Provider to have an issuance and management policy in line with clauses 6 and 7 of it. |
| **[ETSI TS 119 412-6]** | ETSI TS 119 412-6, Certificate profiles for Attestation Providers and Wallet Providers. Requirement ISSU_68 in Topic 10 in Annex 2 of the ARF requires the certificates a PID Provider uses to sign PIDs to comply with it, in particular Clause 4. |
| **[ETSI TS 119 472-3]** | ETSI TS 119 472-3, Electronic Signatures and Trust Infrastructures — Profiles for Attestations of Attributes — Part 3. It profiles the Credential Issuer Metadata a PID Provider publishes, and bears on the issuance provisions to be settled in Sections 5.2 to 5.4. RO_PID_61 requires this Rulebook to be reviewed against it. |
| **[OIDC]** | OpenID Connect Core 1.0. |
| **[OpenID4VCI]** | OpenID for Verifiable Credential Issuance. |
| **[HAIP]** | OpenID4VC High Assurance Interoperability Profile. Sections 4 and 6 profile [OpenID4VCI]; Section 6.1 specifies the IETF SD-JWT VC Profile. |
| **[W3C VCDM v2.0]** | W3C Verifiable Credentials Data Model v2.0. A third attestation format contemplated by Topic 12 in Annex 2 of the ARF, which this Rulebook does not specify. |
| **[Technical Specification 2]** | European Commission Technical Specification 2 — Notification and publication of provider information, referenced by Topic 31 in Annex 2 of the ARF. |
| **[Technical Specification 3]** | European Commission Technical Specification 3 — Wallet Unit Attestation, referenced throughout Topic 9 in Annex 2 of the ARF. It governs the content and processing of the Wallet Instance Attestation and the Key Attestation. |
| **[ECCG Agreed Cryptographic Mechanisms]** | The list of agreed cryptographic mechanisms maintained by the European Cybersecurity Certification Group, version 2.0, referenced by requirements OIA_03 in Topic 1 and WUA_04 in Topic 9 in Annex 2 of the ARF. |
| **[BCP 47]** | Tags for Identifying Languages (RFC 5646 and RFC 4647). |
| **[EKYC]** | OpenID Connect for Identity Assurance 1.0. |
| **[EKYC Schema]** | OpenID Identity Assurance Schema Definition 1.0. |
| **[IANA-JWT-Claims]** | IANA JSON Web Token Claims Registry. |
| **[RFC 2119]** | Key words for use in RFCs to Indicate Requirement Levels. |
| **[RFC 3339]** | Date and Time on the Internet: Timestamps. |
| **[RFC 5322]** | Internet Message Format. |
| **[RFC 7519]** | JSON Web Token (JWT). |
| **[RFC 8610]** | Concise Data Definition Language (CDDL). |
| **[RFC 8943]** | Concise Binary Object Representation (CBOR) Tags for Date. |
| **[RFC 8949]** | Concise Binary Object Representation (CBOR). |
| **[ICAO 9303]** | ICAO Doc 9303, Machine Readable Travel Documents. Part 3 fixes the character set of the machine-readable zone. |
| **[ISO 3166-1]** | Codes for the representation of names of countries and their subdivisions — Part 1: Country codes. |
| **[ISO 3166-2]** | Codes for the representation of names of countries and their subdivisions — Part 2: Country subdivision code. |
| **[ISO 8601-1]** | Date and time — Representations for information interchange — Part 1: Basic rules. |
| **[ISO/IEC 5218]** | Information technology — Codes for the representation of human sexes. |
| **[ISO/IEC 19794-5]** | Information technology — Biometric data interchange formats — Part 5: Face image data. |
| **[ISO/IEC 39794-5]** | Information technology — Extensible biometric data interchange formats — Part 5: Face image data. |

The full reference list of the ARF is in Chapter 10 of the ARF main document.

---

## Annex A — National decision register

*To be established — under analysis.*

> **UNDER REVIEW — N16.** This annex is withdrawn pending decision. It records the national decisions taken in this Rulebook, for the purposes of audit and of notification of the Romanian electronic identification scheme to the Commission. It is to be reconstructed before the scheme is notified.

---

## Annex B — Conformance with Topic 3 in Annex 2 of the ARF

This annex records, requirement by requirement, how this Rulebook satisfies Topic 3 (PID Rulebook) in Annex 2 of the Architecture Reference Framework.

**Assessed against** Topic 3 in Annex 2 of the ARF, which comprises twenty-two requirements: PID_01 to PID_21, and PID_03a.

> **This assessment no longer holds in full.** Chapter 7 is withdrawn in full, as are Sections 5.2 to 5.4, and the rows below whose transposing provision is withdrawn are marked **not currently transposed**, or **partly transposed** where a provision in force satisfies part of the requirement and the withdrawn one carried the rest. They are not defects to be corrected but requirements awaiting a decision recorded in Annex D. The remaining rows are unaffected, Chapters 2, 3 and 4 being where Topic 3 principally lands.

RO_PID_61 requires this assessment to be repeated on publication of a new version of Annex 2 and at least once every twelve months, and requires the version history to record the revision it was last performed against, whether or not anything changed. That date records when this annex was last **verified**, not when it was last **altered**. A reader finding it materially out of step with the current ARF should treat the assessment as unverified and RO_PID_61 as not having been honoured.

| Requirement | Obligation, abridged | Satisfied by |
|---|---|---|
| PID_01 | Comply with all requirements in [PID Rulebook] | Section 1.1, which establishes this Rulebook as a national profile of [PID Rulebook] v1.7; Chapter 8 |
| PID_02 | Issue every PID in both the [ISO/IEC 18013-5] and the [SD-JWT VC] format | RO_PID_03 |
| PID_03 | Optional User opt-out from the portrait; if taken, an empty JSON string or CBOR `bstr` | RO_PID_25, which also makes the opt-out available to every User |
| PID_03a | Relying Party not to retain or export the portrait beyond what data protection law permits | **Not currently transposed** — RO_PID_52 is withdrawn with Sections 5.2 to 5.4; see **N12** |
| PID_04 | Attestation type `eu.europa.ec.eudi.pid.1` | RO_PID_21 |
| PID_05 | Namespace `eu.europa.ec.eudi.pid.1` for the [PID Rulebook] attributes | RO_PID_21 |
| PID_06 | Domestic namespace constructed from the PID_05 identifier plus the country code | RO_PID_21, giving `eu.europa.ec.eudi.pid.ro.1`; RO_PID_18 and RO_PID_22 confine the domestic attributes to it |
| PID_07 | Publish the domestic namespace, with identifiers, definitions, presence and encoding, in an Attestation Rulebook complying with Topic 12 | Sections 2.7 and 3.1.5; Chapter 8; RO_PID_30 |
| PID_08 | Include the [CIR 2024/2977] attributes and metadata as issuer-signed data elements | Sections 2.2 to 2.6 and Section 3.1.2 |
| PID_09 | Encode each attribute as the [PID Rulebook] tables specify | Section 3.1.2 |
| PID_10 | Encode in CBOR per [RFC 8949] | Section 3.1.2, encoding rules |
| PID_11 | At most one attribute per attribute identifier | Section 3.1.2, encoding rules |
| PID_12 | Attribute values valid at the `validFrom` timestamp in the MSO | **Partly transposed** — RO_PID_20 is in force and requires each age assertion to state the position at that timestamp. The general rule, for every attribute, was RO_PID_43, withdrawn with Sections 5.2 to 5.4; see **N12** |
| PID_13 | Have a policy relating `issuance_date` and `expiry_date` to `validFrom` and `validUntil` | RO_PID_14 |
| PID_14 | `vct` a URN in `urn:eudi:pid:`, being `urn:eudi:pid:1` or a domestic type extending it | RO_PID_28, giving `urn:eudi:pid:ro:1` |
| PID_15 | *Empty in the assessed revision of Annex 2 — no obligation arises* | — |
| PID_16 | Publish the domestic type, with claim identifiers, definitions, presence and encoding, in an Attestation Rulebook complying with Topic 12 | Sections 2.7 and 4.1.3; Chapter 8; RO_PID_29 and RO_PID_30 |
| PID_17 | Include the [CIR 2024/2977] attributes and metadata as claims | Sections 4.1.1 and 4.1.2 |
| PID_18 | Encode each claim as the [PID Rulebook] tables specify | Sections 4.1.1 and 4.1.2 |
| PID_19 | Attribute values valid at the `nbf` timestamp | **Partly transposed** — RO_PID_20 is in force and requires each age assertion to state the position at that timestamp. The general rule, for every claim, was RO_PID_43, withdrawn with Sections 5.2 to 5.4; see **N12** |
| PID_20 | Have a policy relating `date_of_issuance` and `date_of_expiry` to `nbf` and `exp` | RO_PID_14 |
| PID_21 | All claims individually selectively disclosable, including nested properties and array entries | **Satisfied, with one departure recorded** — RO_PID_26 states the rule for every top-level property, nested property and array entry. It excepts `iat` in addition to the claims [SD-JWT VC] defines as non-disclosable, and PID_21's own exception reaches only the latter. The departure is recorded here rather than left to be inferred from the provision |

**Three requirements outside Topic 3 are recorded here because Section 5.1 is in force without them.** Requirement **ISSU_21** in Topic 10 in Annex 2 of the ARF requires a PID Provider, before issuing a PID, to verify the Wallet Unit's Wallet Instance Attestation and Key Attestation against a trust anchor in the Wallet Provider List of Trusted Entities, and to verify that neither the Wallet Instance nor the Wallet Secure Cryptographic Device has been revoked. It was transposed by a provision withdrawn with Sections 5.2 to 5.4 and is **not currently transposed**; see **N12** in Annex D.

Requirements **ISSU_19** and **ISSU_19b** in the same Topic are likewise **not currently transposed**. ISSU_19 requires a PID Provider, *for the verification of a Wallet Instance Attestation or a Key Attestation*, to accept the Wallet Provider trust anchors it needs as published by the Commission in the Wallet Provider List of Trusted Entities. ISSU_19b requires it, *for the retrieval and management of trust anchors*, to support Lists of Trusted Entities complying with [ETSI TS 119 602]. The two are the counterpart, on the Wallet Provider side, of the trust anchors this Rulebook notifies under RO_PID_53, and RO_PID_31 presupposes them in obliging DGEP to issue to a Wallet Unit of any recognised Wallet Solution. Neither depends on a withdrawn section, and neither is yet stated in this Rulebook.

**Scope of this assessment.** It covers Topic 3 only. Topic 12 is not assessed here, except for the requirements that Topic 3 imports: PID_06 defers to ARB_10, which applies Topic 12's namespace requirements to domestic namespaces, and ARB_06a is addressed in Chapter 8. ARB_06b, cited in Section 4.1, was verified against the same revision of Annex 2.

---

## Annex C — Conformance with Topic 12 in Annex 2 of the ARF, and with the template for Attestation Rulebooks

This annex records, requirement by requirement, how this Rulebook satisfies Topic 12 (Attestation Rulebooks) in Annex 2 of the Architecture Reference Framework, and how it follows the template for Attestation Rulebooks.

**Assessed against** Topic 12 in Annex 2 of the ARF, which comprises thirty-nine requirements — ARB_01 to ARB_34, together with ARB_01a, ARB_01b, ARB_06a, ARB_06b and ARB_24a — and against version **1.5** of the [Rulebook template].

RO_PID_61 requires this assessment to be repeated on the same terms as the assessment in Annex B.

> **This assessment no longer holds in full**, for the reason given at the head of Annex B. Rows whose satisfying provision is withdrawn are marked accordingly.

**A note on applicability, which governs half of this annex.** Many requirements in Topic 12 are addressed to the Scheme Provider for an Attestation Rulebook *"describing a type of attestation that is a QEAA or a PuB-EAA"*, or *"that is a non-qualified EAA"*. **A PID is none of those three.** Those requirements therefore do not bind this Rulebook by their own terms, and are recorded below as **not applicable**, with a note where this Rulebook satisfies them anyway or where the corresponding obligation reaches it by another route. Recording them as satisfied would misstate the position; omitting them would leave a reader unable to tell whether they had been considered.

### C.1 Topic 12 — Attestation Rulebooks

| Requirement | Obligation, abridged | Position |
|---|---|---|
| ARB_01 | QEAA or PuB-EAA: specify [ISO/IEC 18013-5] and/or [SD-JWT VC] | **Not applicable** — a PID is neither. The formats of a Romanian PID are fixed by PID_04 and PID_05 in Topic 3 and by RO_PID_03, which requires both |
| ARB_01a | Non-qualified EAA: specify one or more of three formats | **Not applicable** |
| ARB_01b | [SD-JWT VC] attestations comply with the IETF SD-JWT VC Profile in [HAIP] Section 6.1 | **Satisfied** — Section 4.1, third paragraph |
| ARB_02 | Analyse whether proximity presentation without the internet must be possible; if so require the mdoc format | **Satisfied** — the analysis is recorded in the opening of Chapter 3, and RO_PID_03 requires the format |
| ARB_03 | MAY require the [SD-JWT VC] format, subject to standardisation | **Not exercised** — RO_PID_03 requires both formats on the basis of PID_02, not of this permission |
| ARB_04 | If a [W3C VCDM v2.0] encoding is specified, reference documents for requesting and verifying it | **Not applicable** — this Rulebook specifies no [W3C VCDM v2.0] encoding |
| ARB_05 | Specify an attestation type unique within the EUDI Wallet ecosystem | **Satisfied** — RO_PID_21 for the mdoc document type and RO_PID_28 for the `vct`, both of which PID_04 and PID_14 constrain |
| ARB_06 | Define all attributes: semantics first, encoding-independently; then the encoding of each | **Satisfied, with one departure of arrangement** — Chapter 2 defines every attribute independently of encoding, as Section 2.1 states, and Chapters 3 and 4 specify the two encodings. The exception is `portrait`: Section 2.2 gives its definition and presence, but the national provisions governing it, RO_PID_24 and RO_PID_25, are gathered in Section 3.2 and are encoding-independent although they sit in the [ISO/IEC 18013-5] chapter. RO_PID_24 makes itself the single home of the attribute so that a party implementing the portrait has one provision to read; the cost is that its placement does not follow the chapter structure |
| ARB_06a | Each attribute defined within a namespace; namespace identifier unique in the ecosystem; attribute identifiers unique within it; syntax and semantics fully defined | **Satisfied** — Sections 2.7 and 3.1.5; Chapter 8 states the reasoning for `eu.europa.ec.eudi.pid.ro.1` and its five attribute identifiers |
| ARB_06b | [SD-JWT VC] claim names are IANA-registered, Public Names, or Private Names specific to the type | **Satisfied** — Section 4.1 states the rule. Section 4.1.1 gives the claims registered in [IANA-JWT-Claims], with the reference for each; Section 4.1.2 gives the remaining claims of [CIR 2024/2977] and [PID Rulebook], which are Private Names of the EU-wide PID rather than of this type; and Section 4.1.3 gives the two domestic claims, which are Private Names specific to this attestation type. Every claim falls in one of the three categories ARB_06b admits |
| ARB_07 | SHOULD consider referring to attributes already in the catalogue of attributes of Topic 25, and to the catalogue of attestation schemes | **Satisfied** — of Topic 25 only CAT_04 carries content in the assessed revision, and it governs a request to include or modify an attribute rather than the referring to one, so no populated catalogue of attributes arises for this Rulebook to draw on. The attributes of Chapter 2 are those of [CIR 2024/2977] and [PID Rulebook]; only the **two** data identifiers of Section 2.7 are new, and they yield five attribute identifiers in the [ISO/IEC 18013-5] encoding. The catalogue of attestation schemes established under Article 8 of [CIR 2025/1569] is addressed at RO_PID_30 and at ARB_33 below |
| ARB_08 | SHOULD take existing conventions for attribute identifiers and syntaxes into consideration | **Satisfied** — the four age attributes use the `age_over_NN` identifier and boolean syntax already conventional in [ISO/IEC 18013-5]; `personal_numeric_code` follows the lower-case underscore convention of the EU namespace |
| ARB_09 | Specify for each attribute whether its presence is mandatory, optional, or conditional | **Satisfied** — the levels table in Section 2.1 maps each [RFC 2119] level used in this Rulebook onto one of the three, and every attribute table states a level |
| ARB_10 | MAY define a domestic namespace; all namespace requirements apply to it | **Satisfied** — RO_PID_21 defines it and RO_PID_22 confines the domestic attributes to it |
| ARB_11 to ARB_21 | QEAA, PuB-EAA or non-qualified EAA: include attributes representing the sets of data in Annexes V and VII of the [Reg. eIDAS 2] | **Not applicable** — a PID is none of the three, and the corresponding content of a PID is fixed by [CIR 2024/2977] and carried in Chapter 2. The trust-anchor location contemplated by ARB_20 and ARB_21 is nonetheless carried, as `trust_anchor` under RO_PID_17 |
| ARB_22 | Specify all technical details necessary for interoperability, security and privacy | **Partly satisfied** — RO_PID_55 fixes the cryptographic algorithms and is in force. The privacy provisions governing per-attestation uniqueness and status-list operation are withdrawn with Sections 5.2 to 5.4 and Chapter 7; see **N12** and **N13** |
| ARB_23 | QEAA or PuB-EAA: specify which revocation mechanism of Topic 7 is supported | **Not applicable by its terms.** It was satisfied nonetheless by RO_PID_56, which is withdrawn with Chapter 7; see **N13** |
| ARB_24 | Non-qualified EAA: specify whether the type must be revocable | **Not applicable** — the revocability of a PID is governed by VCR_01 in Topic 7. The provision that placed the Romanian PID outside the short-lived branch of it, RO_PID_38, is withdrawn with Sections 5.2 to 5.4; see **N12** |
| ARB_24a | If revocable, specify the URL for retrieving the status or revocation lists | **Not currently satisfied** — row 6 of the notification table in RO_PID_53 requires the URL to be notified, but RO_PID_56, which fixed it, is withdrawn with Chapter 7; see **N13** and **N9** |
| ARB_25 | Include `attestation_legal_category` as specified in the template, with the value the template specifies | **Satisfied on the basis of [PID Rulebook] Section 2.6, and departed from as against the template** — Section 2.6 and RO_PID_17 carry the attribute with the value `PID`. The template no longer contains that identifier and its three values do not describe a PID; the disagreement is between the EU instruments, and this Rulebook follows [PID Rulebook]. Section C.2 records the same position against the template's Section 2.1 |
| ARB_26 | Non-qualified EAA: SHOULD define how a Relying Party obtains the trust anchors | **Not applicable** — Chapter 6 and Topic 31 govern the trust anchors of a PID Provider |
| ARB_27 | *Empty in the assessed revision* | — |
| ARB_28 | MAY specify an attribute recording a cryptographic binding to an existing PID or attestation | **Not currently addressed** — RO_PID_37 is withdrawn with Sections 5.2 to 5.4; see **N12**. No such attribute is defined in Chapters 3 or 4 |
| ARB_29 | SHOULD follow the structure and contents of the template | **Satisfied** — see C.2 |
| ARB_30 | For [SD-JWT VC], specify for every claim whether it MUST, MAY or MUST NOT be selectively disclosable | **Satisfied** — RO_PID_26 states the rule once for every top-level property, nested property and array entry, excepting only what [SD-JWT VC] itself excepts |
| ARB_31 | SHOULD define a Type Metadata Document, and it SHOULD contain the Claim Selective Disclosure Metadata | **Satisfied and strengthened** — RO_PID_29 makes both mandatory, and requires the metadata to agree with RO_PID_26 |
| ARB_32 | *Empty in the assessed revision* | — |
| ARB_33 | A registration in the catalogue of attestation schemes references the Rulebook | **Satisfied** — RO_PID_30, second paragraph |
| ARB_34 | Specify whether the attestation is device-bound | **Not currently satisfied** — RO_PID_37, which stated it, is withdrawn with Sections 5.2 to 5.4; see **N12** |

### C.2 The template for Attestation Rulebooks

The template is a recommendation under ARB_29 and not a mandate. Where this Rulebook departs from it, the departure follows the chapter structure of [PID Rulebook], which Section 1.1 adopts and which the template's own Section 1.2 permits.

| Template element | Obligation, abridged | Position |
|---|---|---|
| Front matter | *Author(s)*, *Previous Authors*, and a feedback contact address or issue tracker | **Satisfied** — the author entry names the authority in the form RO_PID_12 fixes, the previous-author entry records that there are none, this being the first edition, and the feedback address is `feedback.pidrulebook@mai.gov.ro` |
| Sections 1.1 to 1.4 | Scope and purpose, document structure, key words, terminology | **Satisfied** — Sections 1.1 to 1.4 |
| Section 1.2 | Each encoding specified in a separate section or chapter | **Satisfied** — Chapters 3 and 4 |
| Sections 2.1 to 2.7 | Attributes and metadata, arranged by presence category | **Satisfied on the substance, by a different arrangement.** The template separates mandatory, optional and conditional attributes into sections; this Rulebook follows [PID Rulebook] and arranges Chapter 2 by the instrument that defines each attribute, stating the presence of each and mapping the levels onto ARB_09's three categories in Section 2.1. No attribute is left without a presence category |
| Section 2.1 | The `category` attribute and its three values | **Departed from deliberately, on the same basis as ARB_25 above** — the template's `category` identifier and its three values do not describe a PID. Section 2.6 and RO_PID_17 carry `attestation_legal_category` with the value `PID`, as [PID Rulebook] Section 2.6 provides |
| Section 3.1 | mdoc encoding: document type, encoding formats and lengths, date rules, canonical CBOR rules, the attribute table, namespace rules | **Satisfied** — Sections 3.1.1 to 3.1.5, whose encoding rules reproduce the template's list |
| Section 3.1 | *"Finally, illustrative examples SHALL be included"* | **Satisfied** — Section 3.3 |
| Section 3.2 | [SD-JWT VC] encoding: the [HAIP] profile, a unique `vct`, claim-name provenance, a selective-disclosure statement for every claim | **Satisfied** — Sections 4.1, 4.1.1 to 4.1.3, 4.2, and RO_PID_26 |
| Section 3.2 | *"Finally, illustrative examples SHALL be included"* | **Satisfied** — Section 4.3 |
| Section 3.3 | [W3C VCDM v2.0] encoding | **Not applicable** — the template makes this section conditional on the type supporting that format, and this Rulebook does not specify it |
| Section 4 | Attestation usage | **Partly satisfied** — Section 5.1, enrolment and issuance, is in force; Sections 5.2 to 5.4, which carry lifecycle, presentation and the restrictions on requesting attributes, are withdrawn; see **N12** |
| Section 5 | Trust anchors | **Satisfied** — Chapter 6 |
| Section 6 | Revocation | **Not currently satisfied** — Chapter 7 is withdrawn; see **N13** |
| Section 7 | Compliance | **Satisfied** — Chapter 8 |
| Section 8 | References | **Satisfied** — Chapter 9 |

**Scope of this assessment.** It covers Topic 12 and the template. Conformance with Topic 3 is recorded in Annex B.

---

## Annex D — Register of provisions under review

This annex registers every provision and section of this Rulebook marked **UNDER REVIEW**. A marking in the text without a row here, or a row here without a marking in the text, is a defect in this Rulebook. Section 1.3 states the convention and the three forms a marking takes.

**Six entries remain.** Three are withdrawn in full — **Chapter 7**, Sections 5.2 to 5.4 and Annex A — and in one, N9, a single value is withdrawn from a provision that otherwise remains in force. Twenty-five identifiers carry no content, and this Rulebook cannot presently be notified, implemented against as a whole, or assessed for conformance. This annex is the list of what has to be settled before it can be.

| # | What is under review | Where | Status |
|---|---|---|---|
| **N6** | The national requirements for the `portrait` attribute | RO_PID_24, and the `portrait` row of the table in Section 2.2 | Drafted and marked |
| **N8** | The division of the duty to keep a valid technical PID available | RO_PID_14 | Drafted and marked |
| **N9** | The URL carried in the `trust_anchor` attribute | RO_PID_17, and the `trust_anchor` row of the table in Section 2.6 | The **value** of `trust_anchor` is withdrawn; RO_PID_17 itself is in force and requires the attribute. The trust-anchor URL in the examples is a placeholder. The status-list URLs are Chapter 7's and fall under **N13** |
| **N12** | Sections 5.2 to 5.4. Reserves RO_PID_33 to RO_PID_52 | Sections 5.2 to 5.4, and the example notes in Sections 3.3 and 4.3 | **Withdrawn** |
| **N13** | Chapter 7. Reserves RO_PID_56 to RO_PID_60 | Chapter 7, and the example notes in Sections 3.3 and 4.3 | **Withdrawn** |
| **N16** | Annex A | Annex A | **Withdrawn** |

**What "withdrawn" means.** The provision or section carries no content. Nothing is required or permitted by it, and no conformance assessment can be performed against it. Annexes B and C mark the requirements that are consequently not transposed. **The drafting is not lost**: the text as it stood is retained by DGEP, so that settling an entry is a matter of restoring and amending rather than of drafting afresh.

**The identifiers of a withdrawn provision are reserved**, as Section 1.3 provides, and a cross-reference to one made elsewhere in this Rulebook is a reference to that provision as it will be settled.

**On closing an entry.** When a matter is settled, the provision is amended, the marking is removed from the text, the row is removed from this annex, and the decision is recorded in Annex A. An entry is not closed by deleting the row alone.
