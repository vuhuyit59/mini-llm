/** @type {import('next').NextConfig} */
const path = require('path');
const {readFileSync} = require('fs');

const nextConfig = {
  swcMinify: true,
  reactStrictMode: true,
  sassOptions: {
    includePaths: [path.join(__dirname, 'styles')],
  },
  i18n: {
    locales: ['en'],
    defaultLocale: 'en',
  },
  compiler: {
    // Enables the styled-components SWC transform
    styledComponents: true,
  },
};

module.exports = nextConfig;
