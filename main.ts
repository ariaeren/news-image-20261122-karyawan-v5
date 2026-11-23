// Deterministic make.fun entrypoint (Node 22, standard library only).
// The committed entry.png is the artwork; this copies it byte-for-byte to the output directory.

import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });

const source = fileURLToPath(new URL('./entry.png', import.meta.url));
const destination = join(outputDir, 'entry.png');
copyFileSync(source, destination);

const bytes = statSync(destination).size;
if (bytes === 0 || bytes > 1_048_576) {
  throw new Error(`entry.png failed the gate size check: ${bytes} bytes`);
}
console.log(`entry.png copied (${bytes} bytes)`);
