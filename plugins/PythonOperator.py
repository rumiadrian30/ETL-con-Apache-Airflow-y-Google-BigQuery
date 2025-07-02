inicio = DummyOperator(task_id='inicio', dag=dag)

dim_tiempo = PythonOperator(
    task_id='cargar_dim_tiempo',
    python_callable=cargar_dim_tiempo,
    dag=dag
)

dim_vehiculo = PythonOperator(
    task_id='cargar_dim_vehiculo',
    python_callable=cargar_dim_vehiculo,
    dag=dag
)

dim_geografia = PythonOperator(
    task_id='cargar_dim_geografia',
    python_callable=cargar_dim_geografia,
    dag=dag
)

dim_propietario = PythonOperator(
    task_id='cargar_dim_propietario_transaccion',
    python_callable=cargar_dim_propietario_transaccion,
    dag=dag
)

fact_matriculas = PythonOperator(
    task_id='cargar_fact_matriculas',
    python_callable=cargar_fact_matriculas,
    dag=dag
)

fin = DummyOperator(task_id='fin', dag=dag)
