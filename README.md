python-patterns
===============

A collection of design patterns and idioms in Python.

When an implementation is added or modified, be sure to update this file and
rerun `append_output.sh` (eg. ./append_output.sh borg.py) to keep the output
comments at the bottom up to date.

Examples and references from: [https://github.com/domnikl/DesignPatternsPHP](https://github.com/domnikl/DesignPatternsPHP) 

Design Patterns:

| Pattern | Description |     |
|:-------:| ----------- | --- |
| [Static factory](static_factory.py) | Class with static method for creating object | [:page_facing_up:](static_factory.py)<br>[:bar_chart:](diagrams/static_factory.png?raw=true) |
| [Simple factory](simple_factory.py) | Single class for creating objects | [:page_facing_up:](simple_factory.py)<br>[:bar_chart:](diagrams/simple_factory.png?raw=true) |
| [Factory method](factory_method.py) | "Define an interface for creating an object, but let the classes that implement the interface decide which class to instantiate. The Factory method lets a class defer instantiation to subclasses." | [:page_facing_up:](factory_method.py)<br>[:bar_chart:](diagrams/factory_method.png?raw=true)<br>[:book:](http://en.wikipedia.org/wiki/Factory_method_pattern) |
| [Abstract factory](abstract_factory.py) | "Provide an interface for creating families of related or dependent objects without specifying their concrete classes." | [:page_facing_up:](abstract_factory.py)<br>[:bar_chart:](diagrams/abstract_factory.png?raw=true)<br>[:book:](http://en.wikipedia.org/wiki/Abstract_factory_pattern) |

All other Patterns: 

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](adapter.py) | adapt one interface to another using a whitelist |
| [borg](borg.py) | a singleton with shared-state among instances |
| [bridge](bridge.py) | a client-provider middleman to soften interface changes |
| [builder](builder.py) | call many little discrete methods rather than having a huge number of constructor parameters |
| [catalog](catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chain](chain.py) | apply a chain of successive handlers to try and process the data |
| [command](command.py) | bundle a command and arguments to call later |
| [composite](composite.py) | encapsulate and provide access to a number of different objects |
| [decorator](decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](facade.py) | use one class as an API to a number of others |
| [flyweight](flyweight.py) | transparently reuse existing instances of objects with similar/identical state | 
| [graph_search](graph_search.py) | (graphing algorithms, not design patterns) |
| [mediator](mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](memento.py) | generate an opaque token that can be used to go back to a previous state |
| [mvc](mvc.py) | model<->view<->controller (non-strict relationships) |
| [observer](observer.py) | provide a callback for notification of events/changes to data |
| [pool](pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |
| [proxy](proxy.py) | an object funnels operations to something else |
| [publish_subscribe](publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [state](state.py) | logic is org'd into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](strategy.py) | selectable operations over the same data |
| [template](template.py) | an object imposes a structure but takes pluggable components |
| [visitor](visitor.py) | invoke a callback for all items of a collection |
| [chaining_method](chaining_method.py) | continue callback next object method |

Abstract factory vs factory method patterns: what's the difference:
-------------------------------------------------------------------

Abstract Factory allows to create several different type of instances in one sub-class, and to particularize the 
creations behavior in its different sub-classes; normally, Factory method declares the creation of only one type 
of object that can be particularized according to the sub-classing mechanism.
[http://stackoverflow.com/questions/4209791/design-patterns-abstract-factory-vs-factory-method](http://stackoverflow.com/questions/4209791/design-patterns-abstract-factory-vs-factory-method)