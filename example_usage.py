from client import StructuredSyntheticDataEvolutionGeneratorClient

def main():
    client = StructuredSyntheticDataEvolutionGeneratorClient()
    res = client.evolve_synthetic_instruction('Explain Dijkstra algorithm', 4, 'DEEPEN_STEP_BY_STEP')
    print('Synthetic Data Evolution: ' + res['dataset_sample_id'] + ' (Verdict: ' + res['quality_filter_verdict'] + ')')
    print('Gain: +' + str(res['complexity_score_gain_pct']) + '%')
    print('Evolved Prompt: ' + res['evolved_prompt_text'])
    print('Manifest URL: ' + res['evolved_dataset_manifest_url'])

if __name__ == '__main__':
    main()
