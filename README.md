# natcap-community-ndr-plus


## Abstract
This prototype is intended to explore the utility and challenges around using a
new namespace package, `natcap.invest.community`, to allow InVEST models to be
developed and maintained outside of the InVEST development cycle but still
within the InVEST ecosystem.

## Use Cases

### NDR+: Someone needs to run NDR with D8

This case came up several times where someone at natcap needed a model that was
a slight but nontrivial adaptation of an existing InVEST model.  Since `git` is
super casual about its branching, storing models as branches in a `git`
repository is surprisingly mutable and we risk accidentally losing a model's
source code as the result of enthusiastic branch cleanup, and so as a result,
the InSPRING repository cropped up as a way to have an API-only model
implementation that existed outside of the InVEST development cycle.  This is,
unfortunately an antipattern of development.  While it's easier to implement
a model outside of InVEST in this way and we don't risk losing the source code
in the same way due to branching, the model is functionally distinct from InVEST
and doesn't have a clear relationship to InVEST proper, nor a clear path
for including its changes into InVEST itself.

A workable solution should allow easy identification of a model and its source code,
support maintenance under varying software licenses, and be independent of the
InVEST release cycle.

### Schistosomiasis: Developing a new InVEST model "research script"

With the upcoming Schistosomiasis work, the intent is to develop a "research
script" that could eventually be added to the InVEST model suite.  Since
software team time is funded, it would make sense to develop this in a way that
makes sense for the project and, if it makes sense to do so and the intent is
indeed to release the model with InVEST, it would be nice to be able to develop
this in a way that the model could be experimented with easily, but not be
an official part of InVEST until the PSC has granted approval.

A workable solution should include a process for an InVEST-like model to be
developed completely independently of the InVEST release cycle, yet be
accessible to research science staff via an InVEST-style interface.

## Proposed solution

`natcap.invest.community` namespace package.

Consequential requirements:

* Reasonable standardization and version control of accepted interfaces.
