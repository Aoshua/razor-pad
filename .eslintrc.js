module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/typescript/recommended'
  ],
	parserOptions: {
    ecmaVersion: 2020
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
	'prefer-const': 0,
	'no-var': 0,
	'no-extra-boolean-cast': 0,
	'@typescript-eslint/no-explicit-any': 'off',
	'@typescript-eslint/no-non-null-assertion': 'off',
	'@typescript-eslint/no-var-requires': 'off',
	'@typescript-eslint/explicit-module-boundary-types': 'off'
  },
  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        mocha: true
      }
    }
  ]
}
