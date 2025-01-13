import styles from './Layout.module.scss';
import React from 'react';
import ResponsiveAppBar from '@/components/AppBar';

export default function Layout({children}: {children: React.ReactNode | React.ReactNode[]}) {
  return (
    <div className={styles.LayoutWrapper}>
      <ResponsiveAppBar />
      {children}
    </div>
  );
}
