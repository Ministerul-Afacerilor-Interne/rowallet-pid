# Romanian PID — Data Model

**Companion to `RO_PID.md`, the Romanian PID Rulebook. Accompanies version 0.1 of that document.**

**Author:** Ministerul Afacerilor Interne, Direcția Generală pentru Evidența Persoanelor<br>
**Version:** 0.1 — 31 Aug 2026<br>
**Feedback:** feedback.pidrulebook@mai.gov.ro<br>
**Status:** **Not normative.** `RO_PID.md` governs; where this document and the Rulebook differ, the Rulebook prevails and this document is to be corrected. RO_PID_61(d) requires each review of the Rulebook to verify that this document still agrees with its Chapters 2, 3 and 4.

---

## Status of this document

This document states the data model of the Romanian Person Identification Data attestation: what a Romanian PID contains, how each attribute is encoded in each of the two mandatory formats, and what a complete attestation looks like in both.

Every requirement stated here is taken from `RO_PID.md`, the Romanian PID Rulebook, and each table cites the provision it derives from. **`RO_PID.md` governs. Where this document and the Rulebook differ, the Rulebook prevails and this document is to be corrected.**

**Part of the Rulebook is withdrawn pending decision, and this document says where.** Six provisions and sections of `RO_PID.md` are marked **UNDER REVIEW** and registered in its Annex D. **Three of the six are withdrawn in full** — **Sections 5.2 to 5.4 of the Rulebook**, **Chapter 7 (revocation)** and Annex A — and in a fourth, N9, a single value is withdrawn from a provision that otherwise remains in force. Twenty-five of its identifiers carry no content. Section 5.1, the enrolment and issuance of a Romanian PID, is in force.

The Rulebook marks an unsettled matter **UNDER REVIEW — N*n*** in three forms, set out in its Section 1.3: the content is withdrawn; or the rule stands and may change; or a single value inside a provision that remains in force is unsettled. This document uses two markings of its own, which map onto those three:

- **WITHDRAWN — N*n*** means the Rulebook provision behind the statement carries no content. What is stated here is what the Rulebook said before the withdrawal, retained so that an implementer can see the shape of what is coming, and it **binds nothing**. Do not build to it expecting it to hold. This is the Rulebook's first form.
- **UNDER REVIEW — N*n*** means the rule stated here is the Rulebook's position and may change, or that the provision is in force while a single value in it is not yet fixed. These are the Rulebook's second and third forms; where only a value is unsettled the text says so.

`RO_PID.md` itself does not use the word *withdrawn* as a marking. It is used here to keep the two cases visibly apart in a document an implementer reads for what to build.

**Annex D of `RO_PID.md` is the register**; this document does not maintain its own. **What is settled** is the structural core and the whole of the attribute set: the two encodings, the document type, the namespaces, the `vct`, the attribute and claim identifiers, their types and their values, the selective-disclosure rule in RO_PID_26, the string-value rule in RO_PID_05, the shape of the age claim in RO_PID_23 and RO_PID_27, and the cryptographic algorithms in RO_PID_55. What is not settled is the **lifecycle and revocation machinery** — Sections 5.2 to 5.4 of the Rulebook and Chapter 7 — the URLs, and the national requirements for the portrait, which RO_PID_24 reserves to itself and which do not bear on phase 1, the value being empty throughout it.

**This document gives no reasons.** For the requirement and its wording, see `RO_PID.md`. For why a value was chosen, why an attribute is issued or declined, and what the alternatives would have cost, see `Rationale.md`.

The examples in Sections 3 and 5 are illustrative, and illustrate a specification that is in part withdrawn: their validity, status and binding elements come from Sections 5.2 to 5.4 of the Rulebook and Chapter 7 of the Rulebook, and several attribute values come from provisions carrying no content. **In Section 3 the salts, the disclosures and the digests are real**: every digest in Section 3.4 is the SHA-256 of the disclosure printed beside it, and the selective-disclosure machinery they demonstrate rests on RO_PID_26, which is in force. **In Section 5 the salts are equally real** — sixteen bytes each, as [ISO/IEC 18013-5] requires at minimum — **but the `valueDigests`, the certificate chain, the payload and the signature are illustrative** and cannot be recomputed from the listing. Signature values are not real in either.

---

## 1 What a Romanian PID contains

A **logical PID** is the person identification data DGEP administers for a User over an administrative validity period measured in years. A **technical PID** is an individual attestation carrying those attributes, issued to a Wallet Unit with its own, much shorter, technical validity period. The length of that period is not settled; Sections 5.2 to 5.4 of the Rulebook will fix it. **WITHDRAWN — N12.**

**RNEP is the authoritative source for every attribute derived from civil-status or population records** (RO_PID_04). DGEP populates no such attribute from another register and none from data the User asserts. The values the Rulebook fixes for itself — `nationality`, `issuing_authority`, `issuing_country`, `attestation_legal_category` and the composition of `place_of_birth` — are not drawn from the register at all; Section 7 lists them. **The CEI — the Romanian electronic identity card — is used for onboarding and is not a source of attribute values**; where a value held on a CEI differs from the value of record in RNEP, RNEP governs and the PID carries the RNEP value.

**Including an attribute obliges nobody to ask for it.** A Relying Party is not required to request every mandatory attribute, and a User is allowed to refuse to present one that is requested. "Mandatory" throughout this document describes what DGEP issues, not what is presented.

**Every logical Romanian PID is issued in both formats** — [ISO/IEC 18013-5] and [SD-JWT VC] — and a Wallet Unit holds both (RO_PID_03). Neither is a fallback for the other: the first serves proximity presentation, the second remote presentation.

**A Wallet Unit holds at most one logical Romanian PID** (RO_PID_01). It holds many technical PIDs for it, issued in batches under rules Sections 5.2 to 5.4 of the Rulebook will settle. **WITHDRAWN — N12.**

### 1.1 The complete attribute set

| Group | Attributes | Source |
|---|---|---|
| Mandatory attributes | `family_name`, `given_name`, `birth_date`, `birth_place`, `nationality`, `portrait` | [CIR 2024/2977] |
| Mandatory metadata | `issuing_authority`, `issuing_country` | [CIR 2024/2977] |
| Optional metadata, **mandatory here** | `expiry_date`, `issuance_date` | [CIR 2024/2977], made mandatory by §2.5 of the Rulebook; RO_PID_13 fixes how `expiry_date` is computed |
| Additional attributes, **mandatory here** | `trust_anchor`, `attestation_legal_category` | [PID Rulebook], made mandatory by §2.6 of the Rulebook; RO_PID_17 fixes the value of `attestation_legal_category` |
| **Domestic attributes** | `personal_numeric_code`, `age_equal_or_over` | RO_PID_18, under PID_06 for the [ISO/IEC 18013-5] encoding and PID_14 with PID_16 for the [SD-JWT VC] encoding |

**`portrait` is issued empty.** Until DGEP announces otherwise, the attribute is present in every Romanian PID and carries the empty value — an empty CBOR `bstr` or an empty JSON string — under the transitional rule in RO_PID_24. It is not omitted, and a Wallet Unit makes its presence and its emptiness evident to the User. **RO_PID_24 is the single provision governing the portrait**, and every further national requirement for it will be added there. **UNDER REVIEW — N6.**

**Once the value is populated it must comply with [CIR 2024/2977]**: the quality requirements for a full frontal image type set out in [ISO/IEC 39794-5], provided as JPEG image data without the headers or blocks specified in clause 5 of [ISO/IEC 19794-5]. Those requirements bind DGEP through that Regulation. Any further national requirement — pixel dimensions, inter-eye distance, the JPEG quality setting, any constraint on the encoded size, and the date from which the value is populated — will be added to RO_PID_24 and nowhere else. **UNDER REVIEW — N6.**

**Every User may opt out of the portrait, and may change that election afterwards** (RO_PID_25). An opt-out does not remove the attribute: it is present and empty, in the same encoding as the transitional rule above prescribes, and no other attribute is withheld because of it. The election is made during issuance. A later change takes effect on the technical PIDs issued after it, by re-issuance of the same logical PID — the administrative validity period does not move — and the superseded technical PIDs are no longer presented, are deleted by the Wallet Unit, and are revoked by DGEP where 24 hours or more of their technical validity remains.

### 1.2 What a Romanian PID does not contain

**No optional attribute of [CIR 2024/2977] is carried.** Each is declined expressly:

| Not carried | Declined by |
|---|---|
| `resident_address`, `resident_country`, `resident_state`, `resident_city`, `resident_postal_code`, `resident_street`, `resident_house_number` | RO_PID_11 |
| `family_name_birth`, `given_name_birth`, `sex` | RO_PID_11 |
| `personal_administrative_number` | RO_PID_10 |
| `email_address`, `mobile_phone_number` | RO_PID_09 |
| `document_number`, `issuing_jurisdiction` | RO_PID_15, RO_PID_16 |

A request for any of these returns nothing. The only persistent identifier a Romanian PID carries is `personal_numeric_code`. The restrictions on requesting it are **WITHDRAWN — N12**; Section 5.4 of the Rulebook will carry them.

### 1.3 The domestic attributes

| Attribute | Value | Provision |
|---|---|---|
| `personal_numeric_code` | The CNP: exactly thirteen decimal digits, no separators, the first in the range 1 to 6 | RO_PID_19 |
| `age_equal_or_over` | Four boolean assertions, at thresholds 14, 16, 18 and 65. All four are always present, whether true or false | RO_PID_20 |

**When the assertions are evaluated.** Each assertion states whether the User had attained that age **at the timestamp in the `validFrom` element of the Mobile Security Object**, for [ISO/IEC 18013-5]-compliant PIDs, and **at the timestamp in the `nbf` claim**, for [SD-JWT VC]-compliant PIDs (RO_PID_20). They are not evaluated at the moment of presentation.

**Both sets are closed.** DGEP issues no domestic attribute beyond the two above and no assertion at any threshold other than the four, in either case without an amendment to the Rulebook (RO_PID_18, RO_PID_20).

**Neither the age assertions nor `birth_date` is derived from the CNP**, although the CNP encodes a date of birth. Both come from the date of birth of record in RNEP (RO_PID_06, RO_PID_20). Where a civil-status rectification has changed the date of birth, RNEP is corrected and the CNP is not.

**RO_PID_19 bars a Relying Party from rejecting a CNP on any ground drawn from the structure of the value** other than the two it states — thirteen decimal digits, the first in the range 1 to 6. The remaining digits encode the date of birth, the county of registration and a sequence number, and none of them is a validity rule the Rulebook states.

**The CNP is the only persistent identifier a Romanian PID carries, and it is a speaking one.** Read on its own it discloses the User's sex, full date of birth and county of registration. A Wallet Unit should make that consequence evident to the User at the point of approval rather than present it as one identifier among others.

`age_equal_or_over` is encoded differently in the two formats; see Section 6.

---

## 2 SD-JWT VC data model

The Verifiable Credential Type is **`urn:eudi:pid:ro:1`**, which extends `urn:eudi:pid:1` and preserves every mandatory claim of the base type (RO_PID_28). A Romanian PID complies with the *IETF SD-JWT VC Profile* in Section 6.1 of [HAIP].

### 2.1 Claims

Strings are UTF-8 and carry Romanian diacritics; see Section 7.

| Claim | Type and format | Presence | Provision |
|---|---|---|---|
| `family_name` | string, upper case; see Section 7 | mandatory | §2.2 of the Rulebook, §4.1.1 of the Rulebook |
| `given_name` | string, upper case. **All of a User's given names are held in one RNEP field and carried as one value**; the Rulebook defines no rule for separating or ordering them | mandatory | §2.2 of the Rulebook, §4.1.1 of the Rulebook |
| `birthdate` | string, [ISO 8601-1] `YYYY-MM-DD` | mandatory | §4.1.1 of the Rulebook |
| `place_of_birth` | object; at least one of `country`, `region`, `locality` present. RO_PID_07 fixes the value, its composition template and what each member carries. **Not upper case** — RO_PID_07 fixes its form and RO_PID_05 does not reach it | mandatory | RO_PID_07, §4.1.1 of the Rulebook |
| `place_of_birth.country` | string, [ISO 3166-1] alpha-2. DGEP derives the code from the country of record in RNEP, which does not hold it as a code | mandatory | RO_PID_07 |
| `place_of_birth.region` | string, **the county written in full** — `Constanța`, not `CT` | present where RNEP records a county; omitted otherwise | RO_PID_07 |
| `place_of_birth.locality` | string, the territorial administrative unit and, where the place of birth is not itself one, the *sat* or *localitate* with its UAT in parentheses. Where no county is recorded, it carries the whole of the recorded place of birth apart from the country | present wherever RNEP records anything below the country | RO_PID_07 |
| `nationalities` | array of strings, [ISO 3166-1] alpha-2. **Exactly one element**, `RO` | mandatory | RO_PID_08 |
| `picture` | string; **the empty string** under the transitional rule in RO_PID_24. Once populated, a `data:` URL carrying the base64-encoded JPEG. **UNDER REVIEW — N6** | mandatory | RO_PID_24, RO_PID_25 |
| `personal_numeric_code` | string, exactly 13 decimal digits, the first in the range 1 to 6 | mandatory | RO_PID_19 |
| `age_equal_or_over` | A JSON object with four boolean members, at thresholds 14, 16, 18 and 65, per RO_PID_20 and RO_PID_27. All four are always present, whether true or false. The member names are decimal strings | mandatory | RO_PID_20, RO_PID_27 |
| `date_of_issuance` | string, `YYYY-MM-DD` | mandatory | §4.1.2 of the Rulebook |
| `date_of_expiry` | string, `YYYY-MM-DD`. The day before the fourth anniversary of `date_of_issuance`; where `date_of_issuance` is 29 February the anniversary is taken as 28 February | mandatory | RO_PID_13, §4.1.2 of the Rulebook |
| `issuing_authority` | string, the fixed value `Direcția Generală pentru Evidența Persoanelor`. Carried in Romanian only: it is not translated, transliterated, abbreviated, or accompanied by a rendering in another language | mandatory | RO_PID_12 |
| `issuing_country` | string, the fixed value `RO` | mandatory | RO_PID_12 |
| `trust_anchor` | string, URL. RO_PID_17 is in force and requires the claim; **the URL it carries is not yet fixed — UNDER REVIEW — N9** | mandatory | RO_PID_17 |
| `attestation_legal_category` | string, the fixed value `PID` | mandatory | RO_PID_17 |

**The member names of `age_equal_or_over` are strings, not numbers** — a JSON object key is a string by definition — and a Relying Party must not rely on their order (RO_PID_27).

**The administrative validity period is four years** (RO_PID_13). `date_of_expiry` is the day before the fourth anniversary of `date_of_issuance`, so the period is exactly four years under the day convention below. It is **not** derived from the expiry of the CEI on which the logical PID was founded, and the administrative validity of a logical Romanian PID is independent of that document.

**How the administrative dates relate to the technical ones (RO_PID_14).** `date_of_issuance` and `date_of_expiry`, and their [ISO/IEC 18013-5] counterparts, carry no time element and none can be encoded. For the purpose of relating them to technical validity, the administrative validity period begins at 00:00:00 on the issuance date and ends at 23:59:59 on the expiry date, **both in the local time of Romania**, converted to UTC wherever a technical field requires an instant. `nbf`/`validFrom` is never earlier than that beginning and `exp`/`validUntil` never later than that end. **DGEP ceases supplying further technical PIDs when the administrative validity period ends**, and **the policy is applied identically to both encodings**, so the administrative dates of the two formats of one logical PID never diverge. Throughout the period DGEP keeps a technical PID with unexpired technical validity available to the Wallet Unit, and RO Wallet requests one; **the division of that duty is UNDER REVIEW — N8**. **A Relying Party determining whether a PID is within its administrative validity period applies that convention and not its own local date** — the two can differ by a day where the Relying Party is in another time zone. The question does not arise for `nbf`, `exp`, `validFrom` and `validUntil`, which carry absolute instants.

**Where the translated name of the authority lives.** `issuing_authority` is carried in Romanian only, but a translated form is available from three places, each of which accommodates more than one language: the Credential Issuer Metadata DGEP publishes, the Type Metadata published under RO_PID_29, and the List of Trusted Entities of PID Providers compiled from the notification made under [CIR 2024/2980]. A Wallet Unit or Relying Party should render the authority name in the language of its interface using those, and transmits the Romanian value unchanged (RO_PID_12).

**What the Type Metadata carries.** RO_PID_29 requires DGEP to author and publish Type Metadata for `urn:eudi:pid:ro:1`. Its `display` array carries entries for **at least Romanian and English**, identified by the `lang` member, whose value is a [BCP 47] language tag, covering the attestation type itself and the domestic claims of Section 2.1. The English rendering of the name of the PID Provider is identical to the one in the Credential Issuer Metadata. The Type Metadata also carries the Claim Selective Disclosure Metadata for every claim, expressing the rule in RO_PID_26.

**What `trust_anchor` is for.** The URL it carries is a convenience for Relying Parties and does not displace the List of Trusted Entities of PID Providers, which is the authoritative source of DGEP's trust anchors and from which a Relying Party obtains them. A Relying Party does not rely on a trust anchor obtained from the `trust_anchor` URL alone where that list is available to it (RO_PID_17, Chapter 6 of the Rulebook).

**Where the claim names come from.** `family_name`, `given_name`, `birthdate` and `picture` are registered claims of Section 5.1 of [OIDC]; `place_of_birth` and `nationalities` come from Section 4.1 of [EKYC]; `date_of_issuance` and `date_of_expiry` are defined in Section 5.4.4.2 of [EKYC Schema]. The remainder are Private Names specific to this attestation type. Requirement ARB_06b requires each to be registered, a Public Name, or a Private Name of the type, and this is the evidence for it.

**No claim of a Romanian PID is conditional as a whole**; every claim above is issued in every Romanian PID. Two nested members are: `place_of_birth.region` is omitted where RNEP records no county, and `place_of_birth.locality` where RNEP records nothing below the country. Both are conditional presence in the sense of ARB_09.

### 2.2 Technical claims

These carry the attestation rather than the User. **[SD-JWT VC] defines which claims are not selectively disclosable; RO_PID_26 excepts those, and adds `iat`.** The Rulebook does not enumerate the first set, so the table below identifies the technical claims a Romanian PID carries and says of each whether it is disclosable — it is not a restatement of the [SD-JWT VC] list.

| Claim | Carries |
|---|---|
| `iss` | The Credential Issuer identifier of DGEP. Not disclosable |
| `vct` | `urn:eudi:pid:ro:1`. Not disclosable |
| `iat` | Issuance instant of this technical PID. [SD-JWT VC] leaves this one disclosable at the issuer's option; **RO_PID_26 excepts it**, so it is carried in the clear |
| `nbf`, `exp` | The technical validity period. Its length is **WITHDRAWN — N12**, Sections 5.2 to 5.4 of the Rulebook being where it will be fixed. RO_PID_14 is in force and requires the technical period to sit inside the administrative one; see the day convention below |
| `status` | The entry of this technical PID in a revocation mechanism, in the form [Token Status List] specifies. **WITHDRAWN — N13**: RO_PID_56 carried it and Chapter 7 is withdrawn in full |
| `cnf` | The public key this technical PID is bound to. **WITHDRAWN — N12**: RO_PID_36 carries the device-binding requirement and Sections 5.2 to 5.4 of the Rulebook are withdrawn |
| `_sd_alg` | The digest algorithm for selective disclosure — `sha-256`. Machinery of [SD-JWT VC] rather than a claim of the attestation, and not disclosable |

### 2.3 Selective disclosure

RO_PID_26 makes **every claim individually selectively disclosable** — every top-level property, every nested property and every array entry — except those [SD-JWT VC] itself defines as non-disclosable, and except `iat`. Section 2.2 identifies the claims a Romanian PID carries in the clear for that reason; it is not an enumeration of the [SD-JWT VC] exceptions, which that specification states and this document does not restate.

This is implemented as follows.

- **`place_of_birth` is recursively disclosable.** The claim is hidden behind a digest in the top-level `_sd`, and its disclosure carries an object containing a further `_sd` array holding the digests of its three members. A Wallet Unit disclosing any member releases two disclosures: the one for `place_of_birth` and the one for the member.
- **`age_equal_or_over` is recursively disclosable on the same pattern.** A Wallet Unit disclosing one threshold releases the `age_equal_or_over` disclosure and that threshold's disclosure, and releases no other.
- **`nationalities` is an array with a disclosable entry.** The disclosed value contains `{"...": "<digest>"}` in place of the element, and the element carries its own disclosure.

The Type Metadata published for `urn:eudi:pid:ro:1` carries the Claim Selective Disclosure Metadata expressing this rule for every claim (RO_PID_29).

---

## 3 SD-JWT VC — worked example

The User in this example was born in Cluj-Napoca on 12 February 1978 and enrolled using an electronic identity card; every attribute value shown is taken from RNEP. It is the User of the example in Section 4.3 of `RO_PID.md`.

### 3.1 The attestation as the User sees it

The claim set a Wallet Unit holds after processing every disclosure. This is **not** what is transmitted; DGEP signs Section 3.3 and issues Section 3.5.

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
  "nationalities": [
    "RO"
  ],
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
  "trust_anchor": "https://<trust-anchor-url>",
  "attestation_legal_category": "PID",
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

Every URL here is a placeholder and none is an endpoint. The trust anchor URL is not settled (**N9**) and the status list URL will be fixed by Chapter 7 of the Rulebook; the Credential Issuer identifier is not fixed by the Rulebook at all.

### 3.2 Protected header

```json
{
  "alg": "ES256",
  "typ": "dc+sd-jwt",
  "x5c": ["MIICyzCCAnGgAwIBAgIU…", "MIIC2DCCAn6gAwIBAgIU…"]
}
```

All three members are required, and none is a national choice.

- **`alg`** is `ES256` — ECDSA with curve P-256 and SHA-256 — which RO_PID_55 requires.
- **`typ`** is `dc+sd-jwt`, which [SD-JWT VC] requires of every SD-JWT VC.
- **`x5c`** carries the issuer's signing certificate and its trust chain. Section 4.1 of the Rulebook makes the *IETF SD-JWT VC Profile* of [HAIP] Section 6.1 binding, and that profile resolves the issuer key through `x5c`; the trust anchor certificate is not included in it. A `kid` in place of `x5c` does not comply.

**The certificate values shown are elided and are not real.** The chain a Relying Party validates is the one whose trust anchor is notified under RO_PID_53 and published in the List of Trusted Entities of PID Providers; Chapter 6 of the Rulebook governs.

### 3.3 Issuer-signed payload

Every attribute is replaced by a digest. Only the technical claims of Section 2.2 appear in the clear.

```json
{
  "iss": "https://<credential-issuer>",
  "vct": "urn:eudi:pid:ro:1",
  "iat": 1788253954,
  "nbf": 1788253954,
  "exp": 1793524354,
  "_sd_alg": "sha-256",
  "_sd": [
    "6P71ghzhNZDJEhallYlDv5CfwqrcW6aE--JG34L_jQQ",
    "7FZ_UBYhdwO-XXizFysMKu2pkjrZCac9y34lxziQzyE",
    "8FnttSkbelYsnyWWyoNqr6B6jRK4kwLpCJfsUCW8UTU",
    "Ag7ean3tYWvHb8inS4NL5g-MgbkdjfnuKHVWOAiKPyM",
    "FXhFX4uOT44NNuWwkZ65I-_aKnWyArdq0kGxcINOfTE",
    "IDfDnFyTqj-ABAP_dGjTLB7NjossSPEQUOpuB7O0ud4",
    "QyBbxl1lkiBb9yW_YXtlsxhAsGOL2K3k8igo3VWaRio",
    "WKPji0dfRF5ZiWZFaCd2WveisXn-Fgr1BF9z_7Sb__c",
    "WKn4wuBJ1_YM__wuPlVeHfy5a1EMe5YdGuojWz68zDs",
    "a8vt_UCasdqesteDt97H2SQA_aY3gFEWadX-r3b33rU",
    "kLQtS1FG13LBARgQTIi2faAeBt1pVqZwB6mFnfsVipA",
    "toYlEKQgQW5HibP9fB7JcytwMYH_5Ql8_u3fP4J0Up4",
    "xhnp0z9fpafMua-NIqLASYWVNBWdNltiCbW2a23Fcw8",
    "zF0gmsgM7fNi-LTV3sNZbjbl3hQ7fHCgusWz8yfElog"
  ],
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

The fourteen digests are the top-level claims. The nested members of `place_of_birth` and `age_equal_or_over`, and the entry of `nationalities`, do not appear here; their digests sit inside their parents' disclosures.

### 3.4 Disclosures

Each disclosure is the base64url encoding, without padding, of a JSON array. For an object property it is `[salt, name, value]`; for an array element it is `[salt, value]`. The digest is the base64url encoding of the SHA-256 of the disclosure string.

**The digest is taken over the disclosure string — that is, over the base64url form in the `Disclosure` column — and not over the JSON.** Any row may be checked with:

```
printf '%s' '<disclosure>' | openssl dgst -sha256 -binary | basenc --base64url | tr -d '='
```

The three disclosures whose value is itself a structure — `place_of_birth`, `age_equal_or_over` and `nationalities` — are shown below as formatted JSON so they can be read, and their base64url form is not printed. To check one, first serialise the JSON compactly, with `", "` between array elements and `": "` after each object key as in every other disclosure here, then base64url-encode it without padding, then hash that. Reformatting the JSON changes the digest.

#### Top-level claims

| Claim | Salt | Disclosure | Digest |
|---|---|---|---|
| `family_name` | `pLetfNC9rA6F4MnGU2Knpw` | `WyJwTGV0Zk5DOXJBNkY0TW5HVTJLbnB3IiwgImZhbWlseV9uYW1lIiwgIlBPUEVTQ1UiXQ` | `6P71ghzhNZDJEhallYlDv5CfwqrcW6aE--JG34L_jQQ` |
| `given_name` | `SfecPJaZKE5iQtIvoeR5Zg` | `WyJTZmVjUEphWktFNWlRdEl2b2VSNVpnIiwgImdpdmVuX25hbWUiLCAiSU9BTi1BTkRSRUkiXQ` | `IDfDnFyTqj-ABAP_dGjTLB7NjossSPEQUOpuB7O0ud4` |
| `birthdate` | `j8qoTcGF0dZi_I_93jwOOw` | `WyJqOHFvVGNHRjBkWmlfSV85M2p3T093IiwgImJpcnRoZGF0ZSIsICIxOTc4LTAyLTEyIl0` | `8FnttSkbelYsnyWWyoNqr6B6jRK4kwLpCJfsUCW8UTU` |
| `place_of_birth` | `lRa50FZ8HHlKGoXLGHmVcg` | *see Section 3.4.1* | `xhnp0z9fpafMua-NIqLASYWVNBWdNltiCbW2a23Fcw8` |
| `nationalities` | `Ya5EYuY9K3B1i3x1rb8FqQ` | *see Section 3.4.3* | `zF0gmsgM7fNi-LTV3sNZbjbl3hQ7fHCgusWz8yfElog` |
| `picture` | `YtAhigznmMhcFSMF4DhBeA` | `WyJZdEFoaWd6bm1NaGNGU01GNERoQmVBIiwgInBpY3R1cmUiLCAiIl0` | `WKPji0dfRF5ZiWZFaCd2WveisXn-Fgr1BF9z_7Sb__c` |
| `personal_numeric_code` | `f0ZAM0BnKVK1rOXTxVgXOQ` | `WyJmMFpBTTBCbktWSzFyT1hUeFZnWE9RIiwgInBlcnNvbmFsX251bWVyaWNfY29kZSIsICIxNzgwMjEyMTIzNDUxIl0` | `toYlEKQgQW5HibP9fB7JcytwMYH_5Ql8_u3fP4J0Up4` |
| `age_equal_or_over` | `OPq2JTXzj-NqNWKg_vdvTw` | *see Section 3.4.2* | `a8vt_UCasdqesteDt97H2SQA_aY3gFEWadX-r3b33rU` |
| `date_of_issuance` | `ok771pnKU-4IcxYEol_p5w` | `WyJvazc3MXBuS1UtNEljeFlFb2xfcDV3IiwgImRhdGVfb2ZfaXNzdWFuY2UiLCAiMjAyNi0wOS0wMSJd` | `QyBbxl1lkiBb9yW_YXtlsxhAsGOL2K3k8igo3VWaRio` |
| `date_of_expiry` | `eMNVnazTTz_xi5WxLAgVRA` | `WyJlTU5WbmF6VFR6X3hpNVd4TEFnVlJBIiwgImRhdGVfb2ZfZXhwaXJ5IiwgIjIwMzAtMDgtMzEiXQ` | `7FZ_UBYhdwO-XXizFysMKu2pkjrZCac9y34lxziQzyE` |
| `issuing_authority` | `--PaERPhhoxUp5V8LMEMeg` | `WyItLVBhRVJQaGhveFVwNVY4TE1FTWVnIiwgImlzc3VpbmdfYXV0aG9yaXR5IiwgIkRpcmVjyJtpYSBHZW5lcmFsxIMgcGVudHJ1IEV2aWRlbsibYSBQZXJzb2FuZWxvciJd` | `Ag7ean3tYWvHb8inS4NL5g-MgbkdjfnuKHVWOAiKPyM` |
| `issuing_country` | `3g_triYgbTs3KbGbRFxiNQ` | `WyIzZ190cmlZZ2JUczNLYkdiUkZ4aU5RIiwgImlzc3VpbmdfY291bnRyeSIsICJSTyJd` | `kLQtS1FG13LBARgQTIi2faAeBt1pVqZwB6mFnfsVipA` |
| `trust_anchor` | `mPyovkZf4mMo8NXPiQkVSw` | `WyJtUHlvdmtaZjRtTW84TlhQaVFrVlN3IiwgInRydXN0X2FuY2hvciIsICJodHRwczovLzx0cnVzdC1hbmNob3ItdXJsPiJd` | `WKn4wuBJ1_YM__wuPlVeHfy5a1EMe5YdGuojWz68zDs` |
| `attestation_legal_category` | `aJvJX1d6TN6bbsn2VjsS0g` | `WyJhSnZKWDFkNlRONmJic24yVmpzUzBnIiwgImF0dGVzdGF0aW9uX2xlZ2FsX2NhdGVnb3J5IiwgIlBJRCJd` | `FXhFX4uOT44NNuWwkZ65I-_aKnWyArdq0kGxcINOfTE` |

The `picture` disclosure carries the empty string, which is what the transitional rule in §3.2 of the Rulebook requires. Once the attribute is populated its disclosure carries the whole base64-encoded JPEG in a `data:` URL, and its digest is over the whole of it.

#### 3.4.1 `place_of_birth` and its members

The disclosed value of `place_of_birth` is an object holding the digests of its three members:

```json
["lRa50FZ8HHlKGoXLGHmVcg", "place_of_birth", {"_sd": [
  "09U9JqKVydevREC7mvIeSkugdbhbLhLrvlgxNkLBntc",
  "I8xmIUCR_VMtb3Kph5fjHHBWeRG24oSvRDgdIWUvPVg",
  "Nz2xTq2pXAU0bbIsJekaFln1zcv08EgfyKNbf2IZ8Vo"
]}]
```

| Member | Salt | Disclosure | Digest |
|---|---|---|---|
| `country` | `zXUF1YG5rYlPSphRyCzWZQ` | `WyJ6WFVGMVlHNXJZbFBTcGhSeUN6V1pRIiwgImNvdW50cnkiLCAiUk8iXQ` | `I8xmIUCR_VMtb3Kph5fjHHBWeRG24oSvRDgdIWUvPVg` |
| `region` | `VUYYX1fYQJRvXWGeMhmcsQ` | `WyJWVVlZWDFmWVFKUnZYV0dlTWhtY3NRIiwgInJlZ2lvbiIsICJDbHVqIl0` | `Nz2xTq2pXAU0bbIsJekaFln1zcv08EgfyKNbf2IZ8Vo` |
| `locality` | `eQDAtRKP9Pxs48xhnPrJAQ` | `WyJlUURBdFJLUDlQeHM0OHhoblBySkFRIiwgImxvY2FsaXR5IiwgIk11bi5DbHVqLU5hcG9jYSJd` | `09U9JqKVydevREC7mvIeSkugdbhbLhLrvlgxNkLBntc` |

**A Wallet Unit disclosing only the country of birth releases two disclosures** — `place_of_birth` and `country`. A member disclosure released without its parent cannot be resolved by a verifier.

#### 3.4.2 `age_equal_or_over` and its members

```json
["OPq2JTXzj-NqNWKg_vdvTw", "age_equal_or_over", {"_sd": [
  "Af8imeeVYOuIML-715seMybPRxhZs9g9WEaE9r3pJd0",
  "K6FyjFOApO5ux9cRzO_LpDrgyKEpi8jpPDjyz0XqjBU",
  "Zyg66Ic98TGJLqDZBFJ4KUsM6O1lzjnP7s1Tb-ZBkP4",
  "iL4NeLLykKXsbL04Dp6-dLvZusz9yw4lb8yb0RQJraI"
]}]
```

| Member | Value | Salt | Disclosure | Digest |
|---|---|---|---|---|
| `14` | `true` | `E3Kz2ACai96MFIFicuXkWA` | `WyJFM0t6MkFDYWk5Nk1GSUZpY3VYa1dBIiwgIjE0IiwgdHJ1ZV0` | `K6FyjFOApO5ux9cRzO_LpDrgyKEpi8jpPDjyz0XqjBU` |
| `16` | `true` | `o0TLQq1qNUocSPHZ5yMbZg` | `WyJvMFRMUXExcU5Vb2NTUEhaNXlNYlpnIiwgIjE2IiwgdHJ1ZV0` | `Zyg66Ic98TGJLqDZBFJ4KUsM6O1lzjnP7s1Tb-ZBkP4` |
| `18` | `true` | `dMnzFQXgaidDvvBu-2RBQg` | `WyJkTW56RlFYZ2FpZER2dkJ1LTJSQlFnIiwgIjE4IiwgdHJ1ZV0` | `Af8imeeVYOuIML-715seMybPRxhZs9g9WEaE9r3pJd0` |
| `65` | `false` | `1_zWv5wj4GE6jaQ1SYOl4A` | `WyIxX3pXdjV3ajRHRTZqYVExU1lPbDRBIiwgIjY1IiwgZmFsc2Vd` | `iL4NeLLykKXsbL04Dp6-dLvZusz9yw4lb8yb0RQJraI` |

**An over-18 check releases two disclosures** — `age_equal_or_over` and `18`. The other three assertions and the date of birth are not disclosed.

#### 3.4.3 `nationalities` and its entry

The disclosed value is an array in which the element is replaced by a digest reference:

```json
["Ya5EYuY9K3B1i3x1rb8FqQ", "nationalities", [{"...": "wzbNU4YJxjHDyzEcCc3TlKXiPkqkB0fKOyWtmYIuGx8"}]]
```

| Entry | Salt | Disclosure | Digest |
|---|---|---|---|
| `[0]` = `"RO"` | `dEhLsfxXcOpA-OKdFDBMSQ` | `WyJkRWhMc2Z4WGNPcEEtT0tkRkRCTVNRIiwgIlJPIl0` | `wzbNU4YJxjHDyzEcCc3TlKXiPkqkB0fKOyWtmYIuGx8` |

By RO_PID_08 the array holds exactly one element. A verifier nonetheless has to handle this form, because RO_PID_26 makes every array entry individually selectively disclosable and RO_PID_29 requires the Type Metadata to say so.

### 3.5 Combined issuance format

DGEP issues the signed JWT followed by all twenty-two disclosures, tilde-separated, with a trailing tilde.

```
<issuer-signed JWT>~WyJwTGV0Zk5DOXJBNkY0TW5HVTJLbnB3IiwgImZhbWlseV9uYW1lIiwgIlBPUEVTQ1UiXQ~WyJTZmVjUEphWktFNWlRdEl2b2VSNVpnIiwgImdpdmVuX25hbWUiLCAiSU9BTi1BTkRSRUkiXQ~…~WyJkRWhMc2Z4WGNPcEEtT0tkRkRCTVNRIiwgIlJPIl0~
```

A Wallet Unit stores all of them, releases only the subset the User has approved, and appends its key-binding JWT at presentation.

---

## 4 mdoc data model

The document type is **`eu.europa.ec.eudi.pid.1`** (RO_PID_21). Attributes are carried in two namespaces:

| Namespace | Content |
|---|---|
| `eu.europa.ec.eudi.pid.1` | The attributes and metadata of [CIR 2024/2977] and [PID Rulebook] |
| `eu.europa.ec.eudi.pid.ro.1` | The Romanian domestic attributes (RO_PID_22). Every domestic attribute sits here; **the structures defined in the EU namespace are not extended with domestic members** |

The domestic namespace identifier is constructed as PID_06 in Topic 3 in Annex 2 of the ARF requires and is not freely chosen.

### 4.1 Attributes

| elementIdentifier | Type | Namespace | Presence |
|---|---|---|---|
| `family_name` | `tstr` | EU | mandatory |
| `given_name` | `tstr` | EU | mandatory |
| `birth_date` | `full-date` | EU | mandatory |
| `place_of_birth` | map with `country`, `region`, `locality`; see the composition rule below | EU | mandatory. `country` is always present; `region` and `locality` are conditional, exactly as in the [SD-JWT VC] encoding |
| `nationality` | array of `tstr` | EU | mandatory |
| `portrait` | `bstr`; **empty** under the transitional rule in RO_PID_24 — **UNDER REVIEW — N6** — raw JPEG once populated | EU | mandatory |
| `expiry_date` | `full-date`. The day before the fourth anniversary of `issuance_date`; where that is 29 February the anniversary is taken as 28 February | EU | mandatory |
| `issuance_date` | `full-date` | EU | mandatory |
| `issuing_authority` | `tstr` | EU | mandatory |
| `issuing_country` | `tstr` | EU | mandatory |
| `trust_anchor` | `tstr`, URL. The claim is required; the URL is **UNDER REVIEW — N9** | EU | mandatory |
| `attestation_legal_category` | `tstr` | EU | mandatory |
| `personal_numeric_code` | `tstr`, 13 digits | RO | mandatory |
| `age_over_14`, `age_over_16`, `age_over_18`, `age_over_65` | `bool`, four separate attributes. RO_PID_23, which fixes this shape, is in force | RO | mandatory |

The type names in the table above — `tstr`, `bstr`, `bool` — are CDDL representation types as defined in [RFC 8610], which is the notation Section 3.1.2 of the Rulebook uses. `full-date` is `#6.1004(tstr)`, tag 1004 per [RFC 8943]. Every `tstr` is UTF-8 and at most 150 characters.

**Dates carry no fraction of a second and no local offset**: the time-offset of [RFC 3339] is `Z` throughout, which governs `signed`, `validFrom` and `validUntil` in the Mobile Security Object (§3.1.2 of the Rulebook).

**Three of the four canonical-CBOR rules of [RFC 8949] §4.2 apply**, and they are: integers of major types 0 and 1 are as small as possible; the expression of the length of a `bstr`, `tstr`, array or map is as short as possible; and indefinite-length items are made definite-length.

**At most one attribute carries any one attribute identifier** — within each namespace and across both namespaces together. The rule is an encoding rule of Section 3.1.2 of the Rulebook, transposing PID_11.

#### 4.1.1 How `place_of_birth` is composed

RO_PID_07 fixes the value and its distribution across the three members, identically in both encodings. For a User born in Romania the recorded place of birth is composed on this template:

```
RO, Jud.JJ Mun./Orș./Loc./Sat./Com.Denumire [(Mun./Orș./Com.Denumire)]*
```

The parenthesised element is used where the User was not born in a territorial administrative unit (*unitate administrativ-teritorială*, UAT) and names the UAT the place of birth belongs to. A UAT is a municipality (*municipiu*), a city (*oraș*) or a commune (*comună*). Besides the UAT, `birth_place` **may** additionally carry the locality (*localitate*) and the village (*sat*); RO_PID_07 permits this and does not require it.

| Recorded value | `country` | `region` | `locality` |
|---|---|---|---|
| `Jud.CT Sat.Darabani (Orș.Negru Vodă)` | `RO` | `Constanța` | `Sat.Darabani (Orș.Negru Vodă)` |
| `Jud.MM Sat.Bârsana (Com.Bârsana)` | `RO` | `Maramureș` | `Sat.Bârsana (Com.Bârsana)` |
| `Jud.CV Sat.Lunga (Mun.Târgu Secuiesc)` | `RO` | `Covasna` | `Sat.Lunga (Mun.Târgu Secuiesc)` |
| `Jud.MM Loc.Iapa (Mun.Sighetu Marmației)` | `RO` | `Maramureș` | `Loc.Iapa (Mun.Sighetu Marmației)` |

**`region` carries the county written in full**, not the two-letter code the register holds. **RNEP does not hold the country of birth as an [ISO 3166-1] alpha-2 code either**, and DGEP derives the code from the country of record. **Where RNEP records no county** — in particular where the User was born outside Romania — `region` is omitted and the whole of the recorded place of birth apart from the country goes into `locality`.

#### 4.1.2 Cryptographic algorithms

RO_PID_55 requires DGEP, RO Wallet and Relying Parties to use only algorithms in the [ECCG Agreed Cryptographic Mechanisms], and fixes these as the minimum for both encodings:

| Purpose | Algorithm |
|---|---|
| The DGEP signature over a technical PID — `issuerAuth` in [ISO/IEC 18013-5], the issuer signature in [SD-JWT VC] | **ECDSA with curve P-256 and SHA-256** |
| Device binding — mdoc authentication, key binding | **ECDSA with curve P-256 and SHA-256** |
| Attribute digests in the Mobile Security Object, and disclosure digests | **SHA-256** |

DGEP may publish further algorithms in a technical profile, each of which must also be in the [ECCG Agreed Cryptographic Mechanisms]. **It may not withdraw an algorithm required above while any technical PID using it remains within its technical validity period.**

### 4.2 Mobile Security Object

| Element | Carries |
|---|---|
| `version`, `digestAlgorithm` | `1.0`, as [ISO/IEC 18013-5] fixes, and `SHA-256`, which RO_PID_55 requires |
| `valueDigests` | One digest per attribute, per namespace |
| `deviceKeyInfo.deviceKey` | The COSE key this technical PID is bound to. **WITHDRAWN — N12** (RO_PID_36) |
| `docType` | `eu.europa.ec.eudi.pid.1` |
| `validityInfo` | `signed`, `validFrom`, `validUntil`. The length of the period is **WITHDRAWN — N12** |
| `status` | The revocation mechanism, which Annex 2 of [CIR 2024/2979] specifies for this encoding. **WITHDRAWN — N13** (RO_PID_56) |

---

## 5 mdoc — worked example

The same User, in the CBOR diagnostic notation of [RFC 8949]. This is the example given in Section 3.3 of `RO_PID.md`, reproduced so that both encodings can be read in one place.

**The `deviceKey` below is not the `cnf` key in Section 3.1.** The two are different technical PIDs of the same logical PID, and the uniqueness rule Sections 5.2 to 5.4 of the Rulebook will settle requires every element capable of being unique — the binding key, every salt, every digest — to differ between them. **WITHDRAWN — N12.**

**The URLs in this example are placeholders and none is an endpoint**, as in Section 3. The `valueDigests` and the elements of `issuerAuth` are illustrative.

### 5.1 `IssuerSigned`

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

### 5.2 `MobileSecurityObject`

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

---

## 6 Differences between the two encodings

The same logical PID is encoded differently in the two formats.

| | mdoc | SD-JWT VC |
|---|---|---|
| Date of birth | `birth_date` | `birthdate` |
| Expiry | `expiry_date` | `date_of_expiry` |
| Issuance | `issuance_date` | `date_of_issuance` |
| Nationality | `nationality` | `nationalities` |
| Portrait | `portrait`, a `bstr` — empty for now, raw JPEG bytes once populated | `picture`, a string — empty for now, base64 in a `data:` URL once populated |
| Values fixed by the Rulebook | `nationality`, `issuing_authority`, `issuing_country`, `attestation_legal_category` and `place_of_birth` are not taken from RNEP; every other string value is carried as RNEP holds it, which for the names means upper case. `portrait` **is** the RNEP facial image, empty only while the transitional rule applies | the same, with `nationalities` for `nationality`; `picture` likewise carries the RNEP image once populated |
| Date format | `full-date`, CBOR tag 1004 | string, `YYYY-MM-DD` |
| **Age assertions** | four separate attributes, `age_over_14` to `age_over_65` | one object `age_equal_or_over` with four members |
| Place of birth members | one indivisible structure — disclosing it discloses country, region and locality together | individually disclosable |
| Nationality entries | whole array only | individually disclosable |

### 6.1 The age assertions

RO_PID_23 fixes the [ISO/IEC 18013-5] encoding and RO_PID_27 the [SD-JWT VC] encoding. In [ISO/IEC 18013-5] the assertions are separate attributes of the domestic namespace, one per threshold; in [SD-JWT VC] they are the members of one object. Implementers are not to reconcile the two.

**The difference is structural only.** In both encodings one threshold may be disclosed without the others.

**Both shapes are settled and in force.** RO_PID_27 fixes the [SD-JWT VC] object form and RO_PID_23 the [ISO/IEC 18013-5] separate attributes. The [SD-JWT VC] claim is **not** encoded as four flat claims matching the mdoc attribute identifiers.

### 6.2 What a Relying Party cannot assume

A request satisfiable in one encoding is not necessarily satisfiable identically in the other. The country of birth may be disclosed alone in a [SD-JWT VC] presentation. It may not in an [ISO/IEC 18013-5] presentation, where `place_of_birth` is presented whole.

---

## 7 String values and matching

Every string in a Romanian PID is carried **exactly as recorded in RNEP**, in UTF-8 (RO_PID_05). **RNEP records names in upper case, with hyphens and with Romanian diacritics**, and the PID carries them in that form. DGEP does not change the case of a value, fold it to ASCII, transliterate it, or remove any character of it.

**A value whose form the Rulebook fixes is not carried as recorded.** `issuing_authority` is the fixed mixed-case string `Direcția Generală pentru Evidența Persoanelor` (RO_PID_12), and `place_of_birth` is composed on the template RO_PID_07 fixes. Neither is affected by the rule above.

**RO_PID_05 states two rules for a Relying Party**: it SHALL NOT refuse a Romanian PID on the ground of the case or the diacritics of a string value, and where it compares a value against its own records it SHOULD normalise both sides by a documented rule rather than require a byte-for-byte match.

The letters `Ă`, `Â`, `Î`, `Ș` and `Ț` occur in Romanian names and are carried as themselves. A value taken from a Romanian PID does not match, byte for byte, the same value read from the machine-readable zone of the User's identity card, which [ICAO 9303] restricts to `A`–`Z`, `0`–`9` and `<`. **The two differ in their diacritics, not in their case:**

| Source | Value |
|---|---|
| Romanian PID | `IONEȘTEANU` |
| Machine-readable zone of the same person's card | `IONESTEANU` |

Both are correct. A Relying Party that enrolled a User by scanning their card and later receives a PID holds two different strings for one name, differing in a single character.

---

## References

| Reference | Document |
|---|---|
| **`RO_PID.md`** | The Romanian PID Rulebook. Governs; this document derives from it. Its **Annex D** registers what is under review. |
| **`Rationale.md`** | The reasoning behind the national decisions this document states. |
| **[CIR 2024/2977]** | Commission Implementing Regulation (EU) 2024/2977 on person identification data and electronic attestations of attributes. |
| **[CIR 2024/2979]** | Commission Implementing Regulation (EU) 2024/2979 on the core functionality of the European Digital Identity Wallet. Its Annex 2 specifies the Attestation Status List mechanism the `status` element uses. |
| **[CIR 2024/2980]** | Commission Implementing Regulation (EU) 2024/2980 on the notification of electronic identification schemes and of providers. The notification from which the List of Trusted Entities of PID Providers is compiled. |
| **[BCP 47]** | Tags for Identifying Languages. The form of the `lang` values in the Type Metadata `display` array. |
| **[PID Rulebook]** | PID Rulebook, ARF Annex 3.01. |
| **[ISO/IEC 18013-5]** | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5. |
| **[SD-JWT VC]** | SD-JWT-based Verifiable Credentials. |
| **[HAIP]** | OpenID4VC High Assurance Interoperability Profile. |
| **[Token Status List]** | Token Status List, the mechanism carrying the `status` claim of a [SD-JWT VC]-compliant PID. |
| **[OIDC]** | OpenID Connect Core 1.0. Source of the registered claim names used in Section 2.1. |
| **[EKYC]** | OpenID Connect for Identity Assurance 1.0. Source of `place_of_birth` and `nationalities`. |
| **[EKYC Schema]** | OpenID Identity Assurance Schema Definition 1.0. Source of `date_of_issuance` and `date_of_expiry`. |
| **[ECCG Agreed Cryptographic Mechanisms]** | The list of agreed cryptographic mechanisms maintained by the European Cybersecurity Certification Group, from which RO_PID_55 requires every algorithm to be drawn. |
| **[ISO/IEC 39794-5]** | Information technology — Extensible biometric data interchange formats — Part 5: Face image data. |
| **[ISO/IEC 19794-5]** | Information technology — Biometric data interchange formats — Part 5: Face image data. |
| **[ICAO 9303]** | ICAO Doc 9303, Machine Readable Travel Documents. |
| **[ISO 3166-1]** | Country codes. |
| **[ISO 8601-1]** | Date and time representations. |
| **[RFC 3339]** | Date and Time on the Internet: Timestamps. Fixes the form of the date and date-time strings this document describes. |
| **[RFC 8610]** | Concise Data Definition Language (CDDL). The source of the representation types — `tstr`, `uint`, `bstr`, `bool`, `tdate` — used in Section 4. |
| **[RFC 8943]** | CBOR Tags for Date. |
| **[RFC 8949]** | Concise Binary Object Representation (CBOR). |
