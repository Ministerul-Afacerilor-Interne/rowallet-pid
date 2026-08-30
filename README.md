# Romanian PID Rulebook

The national Rulebook for natural-person **Person Identification Data (PID)** issued in Romania: how a Romanian PID is composed, encoded, issued and presented within the national European Digital Identity Wallet ecosystem. It is a national profile of the EU PID Rulebook (ARF Annex 3.01) - it restates the requirements that apply to Romanian PIDs and adds the provisions the EU instruments leave to Member States.

Authored and maintained by the Ministry of Internal Affairs, Direcția Generală pentru Evidența Persoanelor (**DGEP**), the PID Provider. The Wallet Provider is the Ministry of Internal Affairs, Direcția Generală pentru Comunicații și Tehnologia Informației (**DGCTI**).

## Status

**Version 0.1 - Phase 1 Draft, 31 August 2026.** Four things to know before reading further:

- **Scope.** This version governs the issuance of Romanian PIDs to **Romanian citizens**. The issuance of a PID to a foreign national resident in Romania is out of scope of this version.
- **The Rulebook cannot presently be notified or assessed as a whole.** Sections 5.2 to 5.4, Chapter 7 and Annex A carry no content, and 25 of the 61 provision identifiers are reserved against them. This is the intended state of a phase 1 draft, not an oversight. **Annex D** registers what is open; **Annexes B and C** record, requirement by requirement, what is and is not transposed.
- **Provision identifiers are not stable between draft versions.** While the Rulebook is a draft the numbering closes up whenever a provision is removed, so a citation should name the version it was taken from. From the first published version onwards an identifier will be retired rather than reassigned.
- Text marked **`UNDER REVIEW`** is unsettled. Where such a passage reads *"To be established - under analysis"*, nothing is required by it and it cannot be implemented against.

## The documents

| File | | |
|---|---|---|
| **`RO_PID.md`** | **Normative** | **The Rulebook.** Where anything else differs from it, it governs |
| `RO_PID_Data_Model.md` | Not normative | The data model for implementers — the attributes, claims and encodings of Chapters 2 to 4 in one place, with a worked example of a complete attestation in each format |
| `Rationale.md` | Not normative | Why each national decision was taken, and what the alternatives would have cost |

Where a provision of this Rulebook is inconsistent with the EU PID Rulebook, [CIR 2024/2977] or the European Digital Identity Regulation, those instruments prevail. Where either companion differs from `RO_PID.md`, the Rulebook prevails and the companion is to be corrected.

## EU baseline

This Rulebook profiles the **PID Rulebook (ARF Annex 3.01) version 1.7, dated 17 July 2026**, and version **1.5** of the template for Attestation Rulebooks, dated 8 July 2026. It was assessed against the revisions of Annex 2 of the ARF in force on **4 August 2026** for Topic 3, recorded in Annex B, and on **7 August 2026** for Topic 12, recorded in Annex C. RO_PID_61 governs review against later versions of those documents and of the Implementing Regulations this Rulebook depends on.

## Feedback

`feedback.pidrulebook@mai.gov.ro`
