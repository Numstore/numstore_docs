<script lang="ts" setup>
import {defineComponent, h, onMounted, type PropType, type Ref, ref} from 'vue'

interface TocNode {
  id: string
  text: string
  level: number
  children: TocNode[]
}

const toc: Ref<TocNode[]> = ref([])

onMounted(() => {
  const root = document.getElementById('documentation')
  if (!root) return

  const heads = root.querySelectorAll<HTMLHeadingElement>('h1,h2,h3,h4')
  const tree: TocNode[] = []
  const stack: TocNode[] = []

  heads.forEach(h => {
    const level = Number(h.tagName[1])
    h.id = (h.textContent || '').trim().toLowerCase().split(' ').join('-')

    const node: TocNode = {id: h.id, text: h.textContent || '', level, children: []}

    while (stack.length && level <= stack[stack.length - 1].level) {
      stack.pop()
    }

    (stack.length ? stack[stack.length - 1].children : tree).push(node)
    stack.push(node)
  })

  toc.value = tree
})

const TocBranch = defineComponent({
  name: 'TocBranch',
  props: {
    item: {type: Object as PropType<TocNode>, required: true}
  },
  setup(props) {
    return () =>
        h('li', {class: 'mb-1'}, [
          h(
              'a',
              {href: `#${props.item.id}`, class: 'text-blue-600 hover:underline'},
              props.item.text
          ),
          props.item.children.length
              ? h(
                  'ul',
                  {class: 'list-disc ml-6'},
                  props.item.children.map(child => h(TocBranch, {item: child}))
              )
              : null
        ])
  }
})
</script>

<template>
  <div class="w-[64rem] mx-auto bg-yellow-500 gap-8">
    <!-- Table of contents -->
    <ul class="list-disc ml-6">
      <TocBranch v-for="n in toc" :key="n.id" :item="n"/>
    </ul>

    <!-- Your document -->
    <div id="documentation" class="">
      <h1>Numstore</h1>
      Numstore is a database that stores C-style binary array data. To understand this distinction further, first let's
      enter "C-land". C's type system, while simple, maps cleanly onto foundational type-theoretic constructs. It
      includes:

      <ul class="list-disc ml-6">
        <li>
          <em>Primitive types</em> like uint8_t, float, and double, which serve as base atomic types.
        </li>
        <li>
          <em>Product types</em>, represented by struct and arrays. Both combine multiple values into a single compound
          type,
          with struct offering heterogeneous products (named fields of differing types) and arrays offering homogeneous
          products (indexed fields of the same type). While arrays are technically just uniform products, they are
          common enough to be treated as a distinct built-in abstraction.
        </li>
        <li>
          <em>Sum types</em>, represented by union, which allow a value to take on the form of one of several types, but
          only one
          at a time—this is a disjoint union, though without tags.
        </li>
        <li>
          <em>Enumerated types</em>, or enum, are finite sets of named constants and can be viewed as simple sum types
          with no associated data - essentially tagged unit types.
        </li>
      </ul>

      From these basic building blocks, programmers can build powerful imitations of what more complex type systems
      offer. For example, the tagged union mimics polymorphism, while keeping the memory footprint of the largest
      implementation:
      <pre>
typedef struct
{
  enum
  {
    SHAPE_CIRCLE,
    SHAPE_RECTANGLE
  } type;

  int id;
  const char *owner;

  union
  {
    struct
    {
      float radius;
    };
    struct
    {
      float width, height;
    };
  };
} shape_t;

static inline float
shape_area (const shape_t *s)
{
  switch (s->type)
    {
    case SHAPE_CIRCLE:
      return (float)M_PI * s->radius * s->radius;

    case SHAPE_RECTANGLE:
      return s->width * s->height;
    }
  UNREACHABLE ();
}
      </pre>

      C's type system is powerful because it's simple, but more importantly, it maps 1-1 to memory layout. You
      don't need to read through any specifications to understand that the following struct:
      <pre>
#pragma pack(push, 1)
typedef struct {
  uint32_t i;
  uin8_t j[10][5];
} foo;
#pragma pack(pop)
      </pre>

      Might look something like this in memory:
      <pre>
[4 bytes] [ [[4 bytes], [4 bytes], ... x5], [[4 bytes], [4 bytes], ... x5], ... x10 ]
      </pre>

      Of course, my `foo` struct is guarded with the `pack` pragma because C has the notion of alignment.
      In general, in Numstore <em>there is no concept of alignment</em> and the previous struct maps directly
      with the expected layout.

      Numstore thrives on binary data.

      <h2>Comparison with other Databases</h2>
      Numstore is not meant to replace object/relational/SQL databases. Nor is it a <em>vector database</em>
      as the term is used to denote databases that measure similarity of data. Rather, it's meant to serve its own
      unique roll in the world of databases.
      <h2>Usecases</h2>
      <ul class="list-disc ml-6">
        TODO
        <li>Machine Learning: Numstore stores data exactly how a numpy/pytorch/tensorflow array/tensor expects it.</li>
        <li>
          Signal Processing: Numstore achieves 10MB of insert bandwidth, meaning it's on the order of your standard
          run of the mill hobbist oscilloscpe to write incomming data. How did I get here:
          <ul>
            <li>Numstore can process 10MB / second</li>
            <li>10MB / 16 bytes per complex float32 = TODO</li>
          </ul>
        </li>
      </ul>
      <h2>What can Numstore <em>not</em> do?</h2>
      Numstore is not a replacement of SQL, or other common data. Specific, numstore is not designed to model
      object relations. Be it foreign keys or heirarchies. Numstore is meant to store large amounts of
      simple single data points that don't implicitly relate to one another.
      <h2>Features Overview</h2>
      <h2>Features Cheat sheet</h2>

      <h2>Getting Started</h2>
      <h3>Linux</h3>
      <h3>Windows</h3>
      <h3>Mac</h3>
      <h2>Main Concepts</h2>

      <h3>Vocabulary</h3>
      <h4>Variable</h4>
      Numstore has a key:value relationship between a <em>variable</em> name (the key) and <em>variable</em>
      data.
      <h4>Type</h4>
      <h4>Array</h4>

      <h3>Types</h3>
      <h4>Primitive</h4>
      <h4>Struct</h4>
      <h4>Union</h4>
      <h4>Enum</h4>
      <h4>Array</h4>

      <h3>Variable Operations</h3>
      <h4>Create</h4>
      <h4>Delete</h4>
      <h4>Insert</h4>
      <h4>Remove</h4>
      <h4>Append</h4>
      <h4>Take</h4>
      <h4>Update</h4>

      <h3>Per Variable Configuration</h3>

      <h3>Per File Configuration</h3>

      <h2>Interfaces</h2>

      <h3>Command Line Interface (CLI)</h3>
      <h3>TCP</h3>
    </div>
  </div>
</template>

<style scoped>
@reference "tailwindcss";
h1 {
  @apply text-4xl font-bold leading-tight;
}

h2 {
  @apply text-3xl font-bold leading-tight;
}

h3 {
  @apply text-2xl font-bold leading-tight;
}

h4 {
  @apply text-xl  font-bold leading-tight;
}

</style>
