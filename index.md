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

### question

answer

### question

answer
