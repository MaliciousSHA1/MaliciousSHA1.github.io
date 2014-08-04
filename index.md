% Malicious SHA-1

<nav>
<hr />
<big>
<b>
<a href="#details">Technical details</a>
&nbsp;&nbsp;
<a href="#downloads">Downloads</a>
&nbsp;&nbsp;
<a href="#faq">FAQ</a>
</b>
</big>
<hr />
</nav>


This is the webpage of the Malicious SHA-1 project, a research project
that demonstrates how the security of the [SHA-1](TBD) hashing standard
can be *fully compromised* if one slightly tweaks some of the predefined
constants in the SHA-1 algorithm.
That is, we show that applications using "custom" versions of SHA-1 may
include backdoors exploitable by the application designers (and only
them).
Such "custom" versions are typically found in proprietary systems as a
way to personalize the cryptography for a given customer, while
retaining the security guarantees of the original algorithm.

The colliding messages constructed can be valid archives files (RAR or
7zip) such that the content of the two archives can be fully controlled.
We also build colliding JPEG files, which can be any two images, as in
the example below: 

![example]()

We can also construct *colliding executables*, which MBR (Master Boot
Record) or COM files including arbitrary code.
Furthermore, we present *polyglot* collisions, that is, two distinct
files that are each both valid MBR code, RAR archives, and shell script;
and such that the respective content of each of those three file formats
can be fully controlled, independently of the other formats.



Implications of this research are discussed in our [FAQ](#faq).

The Malicious SHA-1 project is a joint work of

* [Ange Albertini](https://code.google.com/p/corkami/)
* [Jean-Philippe Aumasson](https://131002.net)
* [Maria Eichlseder]()
* [Florian Mendel]()
* [Martin Schlaeffer]()


## Technical details
<name ="details"/>

The security of a cryptographic hash function such as SHA-1 relies on
the practical impossibility to find collisions, that is, distinct
messages having the same hash value.
We thus show that, with only minor tweaks of the SHA-1 specifications
(namely, about 40 bits of the 128-bit predefined constants), 

Full details can be found in the [research paper](malsha1-yyyymmdd.pdf).

## Downloads
<name ="downloads"/>


## FAQ
<name ="faq"/>

### What are the implications for SHA-1's security?

None. 

The differential cryptanalysis techniques used to find our collisions
are inspired and derived from the best known attacks on the original
SHA-1, and do not lead to improved attacks on SHA-1 (as far as we can
tell).

### Did NSA use this trick when creating SHA-1 in 1995?

We believe this is unlikely, for

1. Our results rely on state-of-the-art differential cryptanalysis
research, as of 2014, based on techniques that were only publicly
developed since around 2004

2. Just before SHA-1, NSA designed SHA-0, for which weaknesses were
quickly identified by the research community and actual collisions
presented later, in 1998; this negligence does not suggest extraordinary
cryptanalysis abilities from NSA back then


### Can you do the same for SHA-256?

Not at the moment.

[SHA-256]() is a much different case, for

1. SHA-256 uses 64 distinct constants for each of its 64 steps, whereas
SHA-1 uses 4 distinct constants for each 20-step "round" of its 80-step
construction. This provides much more freedom to sabotage the algorithm,
however this will likely imply many more differences (in terms of
Hamming weight) than in the case of SHA-1.

2. Whereas theoretical attacks are known on the full, 80-step, SHA-1,
the best known collision attacks on SHA-256 are on [31 steps only](TBD),
of 64 steps in total. It may thus be difficult to find a 64-step
characteristics exploitable to build a malicious SHA-256.
