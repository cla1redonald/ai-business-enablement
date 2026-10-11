# Enabler 1: Trusted information

*Can AI reach information that can be trusted?* Four areas. Nothing else works if AI
cannot reach what it needs, or cannot rely on what it finds.

## 1. System connectivity

**Definition.** Whether the systems the business runs on are reachable by its AI tools
through governed connectors, and whether the approval practice behind the estate leaves
evidence. Connecting the productivity estate is not the same as connecting the business:
the systems that hold the organisation's own operating data are the ones that matter most
and are usually the ones AI cannot reach.

**What to look for.** The connector list, and which class of system each connector
reaches (productivity tools versus systems of record). Which connectors people describe
as genuinely working rather than tolerated. Anything network-bound (behind a VPN or on a
private subnet) that hosted connectors cannot reach. Whether an approval record exists:
what each connector was approved against, by whom. Whether the default direction of
travel (growing the estate) has been reconciled with the tightening direction (read-only
defaults, named approval) or left to resolve itself.

**How to surface it.** Ask IT for the connector list and walk it together (direct
examination; conversations alone will miss it). "Which connectors do people actually
rely on?" "Which systems hold your own operating data, and can any AI tool reach them
today?" "What was this connector approved against, and where is that recorded?"

**Rating anchors.**
- In place: both productivity systems and systems of record reachable through approved
  connectors, with an approval record a certification audit could read.
- Partial: the productivity estate connected and working; the systems holding operating
  data unreachable, or the approval practice real but leaving no evidence.
- Gap: little or no governed connectivity; connections are personal improvisations.
- Blocked: a named system everything wants is prevented by a network or security
  boundary with no agreed route. (A blocked sub-item can sit inside a partial area;
  count it separately.)

## 2. Knowledge and document access

**Definition.** Whether the file and knowledge layer is structured, current and reachable
so AI can find the canonical version of what it needs. The underlying issue is almost
always structure rather than tooling: a migrated-not-reorganised estate defeats retrieval
regardless of the tool over it.

**What to look for.** What the file layer is and how recently it changed. Whether content
was migrated as it stood or reorganised. How many habits run in parallel (native AI in
the file tool, connectors, local sync only). Whether a taxonomy or naming convention
exists and who owns it. Whether "finding things" appears unprompted in staff complaints.
Which knowledge tools each population uses (engineering often lives somewhere the rest
of the business does not). Any common file type AI cannot reach at all.

**How to surface it.** "Walk me through where a document lives from creation to being
found by someone else." "What can you never find?" "If your AI assistant answered from
your files today, would you trust the version it found?" Ask leadership what complaint
they hear most about information.

**Rating anchors.**
- In place: one agreed layer, a taxonomy in use, AI reaches current canonical content,
  and someone owns the structure.
- Partial: the layer chosen and syncing but structure undecided or migrated as-was;
  parallel habits; findability a live complaint.
- Gap: no agreed layer, or the estate so scattered that no retrieval can be trusted.
- Blocked: a decision or migration everything waits on, with no owner or date.

**Sequencing note.** Structure first, then retrieval, then anything semantic. A retrieval
layer over an unstructured estate returns confident answers from badly organised
material. A cheap index of what exists, where the canonical version lives and who owns it
removes most of the guessing before any platform is bought, and is cheap to abandon.
Structuring information for people and structuring it for AI are different exercises;
department leads own the first, IT must set out the second.

## 3. Data boundaries

**Definition.** Whether it is decided, and written down, which categories of the
organisation's data may enter an AI tool, under what conditions. The thinking is often
done before the artefact exists, and the artefact is what a client due-diligence
questionnaire asks for first.

**What to look for.** A data classification policy, and whether it has been mapped to AI
use. Hosting jurisdiction decisions and their rationale (accreditation-based approval is
a pattern that generalises). Whether anonymisation or tokenisation is practised by
design. Whether anyone can answer "may this class of data enter this tool?" without
convening a meeting. Usually needs direct examination: read the policy set rather than
waiting for it to come up.

**How to surface it.** "Which categories of data may go into an AI tool today, and where
is that written?" "What would you show a client who asked?" "What was the basis for
accepting your AI supplier's hosting arrangements?"

**Rating anchors.**
- In place: a written mapping from the existing data classifications to AI use, current
  and known to the people who need it.
- Partial: the underlying position strong and deliberate (classification exists,
  jurisdictions decided, anonymisation practised) but no written AI mapping.
- Gap: no classification, or AI use proceeding with no considered position on what may
  enter it.
- Blocked: a legal or regulatory question formally unresolved that suspends AI use of a
  data class.

## 4. Internal data

**Definition.** Whether the organisation's own operating data has a governed, queryable
home with ownership: a warehouse or equivalent, a BI capability over it, and a role that
owns data strategy. Distinct from product or customer data, which may be excellently
managed while the internal estate is not ("good with client data, not as good with our
own" is the recurring shape).

**What to look for.** Whether an internal warehouse or lake exists at all. Whether a BI
function exists, or one tool acts as its stand-in and who its custodians are. How many
separate systems hold operating data (CRM, finance, recruitment, tickets, security
evidence, documents) and whether any inventory of them exists. Which recurring outputs
are assembled by hand from copy and paste. Who, if anyone, owns data governance,
dictionary, pipelines and architecture; whether those decisions have a home at executive
level or fall to whoever is nearest.

**How to surface it.** "Is there a single place your own operating data lives? If not,
where does the monthly reporting actually come from?" "Who decides whether a warehouse
gets built?" "What does your most senior finance person name as the biggest data
opportunity?" Ask finance to describe one recurring number's journey end to end.

**Rating anchors.**
- In place: a governed, queryable home for internal data with named ownership and a BI
  capability the business trusts.
- Partial: a warehouse or BI layer exists for part of the estate, or a funded build is
  under way with an owner and a date.
- Gap: no warehouse, no BI function, no inventory, and the ownership decisions have no
  home. This is commonly the largest single unlock in a discovery and the one with no
  clear owner; say both.
- Blocked: the build formally waits on another programme (identity, a migration) with
  the dependency named.

**Sequencing note.** The action is rarely "build a warehouse now". It is to get to a
decision with a mandate and a date: a named executive, a scoped piece of work to
establish what a minimum useful internal data capability would cost and cover, and a date
by which the answer is due. The decision can legitimately be "not yet"; it cannot be
undecided by default.
