import { useEffect, useState } from 'react';

type Snapshot = {
  symbol: string;
  price: number;
  change_pct_daily: number;
};

type Score = {
  direction: string;
  score: number;
  confidence: string;
};

export default function Home() {
  const [snapshots, setSnapshots] = useState<Snapshot[]>([]);
  const [score, setScore] = useState<Score | null>(null);

  useEffect(() => {
    const load = async () => {
      const [s, m] = await Promise.all([
        fetch('http://localhost:8000/api/v1/snapshots').then((r) => r.json()),
        fetch('http://localhost:8000/api/v1/macro-score').then((r) => r.json()),
      ]);
      setSnapshots(s);
      setScore(m);
    };

    load();
    const t = setInterval(load, 5000);
    return () => clearInterval(t);
  }, []);

  return (
    <main style={{ fontFamily: 'Inter, sans-serif', padding: 24, background: '#0b1020', minHeight: '100vh', color: '#fff' }}>
      <h1>APPMacroGold Dashboard</h1>
      <p>Monitoramento macro para confirmação operacional de XAUUSD.</p>

      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(180px,1fr))', gap: 12, marginTop: 20 }}>
        {snapshots.map((item) => (
          <article key={item.symbol} style={{ background: '#151c31', borderRadius: 12, padding: 12 }}>
            <strong>{item.symbol}</strong>
            <div>{item.price.toFixed(4)}</div>
            <div style={{ color: item.change_pct_daily >= 0 ? '#00d68f' : '#ff5f6d' }}>{item.change_pct_daily.toFixed(2)}%</div>
          </article>
        ))}
      </section>

      {score && (
        <section style={{ marginTop: 20, background: '#151c31', padding: 16, borderRadius: 12 }}>
          <h2>GOLD {score.direction} SCORE: {score.score}/100</h2>
          <p>Confiança: {score.confidence}</p>
        </section>
      )}
    </main>
  );
}
