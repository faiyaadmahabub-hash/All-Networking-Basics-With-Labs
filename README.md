# Networking Fundamentals — Packet Tracer Labs

A learning archive of **30 Cisco Packet Tracer exercises** covering introductory networking. These are course-origin activities and saved topology files, not 30 independently authored applications.

**Status:** all files inventoried and hashed; completion scores and live network behavior were not rechecked.

## Skills covered

| Area | Practice |
|---|---|
| IOS and basic devices | CLI navigation, switch/router setup and interface configuration |
| Addressing | IPv4 subnetting, VLSM and IPv6 |
| Protocol behavior | OSI/TCP-IP models, ICMP, TCP and UDP |
| Verification | Ping, traceroute and `show` output |
| Security | SSH, passwords and basic device hardening |
| Troubleshooting | Gateway faults and integrated challenges |

```mermaid
flowchart LR
    A[Read activity instructions] --> B[Plan addressing]
    B --> C[Configure devices]
    C --> D[Test connectivity]
    D --> E[Inspect activity results]
```

## Use the archive

Open a `.pka` or `.pkt` in a compatible Cisco Packet Tracer 8.x installation. Work in numeric course order and save your changes separately. `.pka` files include activity instructions/scoring; `.pkt` files are standalone topologies. The two module-2 video activities are `.pkt` files.

The [detailed lab index](docs/PROJECT_GUIDE.md#lab-index) maps each filename to its exercise and starting topology. Missing course modules are not supplied here.

## Verification and portfolio scope

```bash
python docs/verify_offline.py
```

The fresh inventory confirms **28 activities and 2 topologies**, all non-empty. Hashes identify the files reviewed. This does not establish completion, a particular score or functioning routing; those require opening each activity and checking it in Packet Tracer.

No desktop simulation capture was available, so this README makes no fresh screenshot or connectivity claim. A stronger future portfolio addition would pair a completed lab's actual score with a short explanation of the fault fixed and verified packet path.

## Attribution and documentation

The activity text, topology templates and scoring originate from Cisco Networking Academy coursework. This archive records learning practice; ownership of the original teaching material is not claimed.

- [Full exercise index and walkthrough](docs/PROJECT_GUIDE.md)
- [Verification scope](docs/VERIFICATION.md) and [file hashes](docs/results.txt)
